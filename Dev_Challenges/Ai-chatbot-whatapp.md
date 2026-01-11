
# Solution Overview

Use n8n to handle incoming WhatsApp chats (via a WhatsApp API provider) and call an AI (e.g. OpenAI GPT) to converse and take orders. A high-level workflow is:

- **Choose a WhatsApp API gateway** (since there’s no WhatsApp Business account). For example, UltraMsg or Twilio Sandbox. UltraMsg provides a simple REST API for WhatsApp (has a 3-day free trial then $39/mo), while Twilio’s free Sandbox lets you test WhatsApp messaging without initial cost. Either way, sign up and obtain credentials (UltraMsg gives an Instance ID and Token).
    
- **Host n8n on a low-cost server.** You can self-host n8n (e.g. in Docker on a free-tier VPS like Oracle Cloud’s free VM) and expose it via HTTPS (with a proper domain or tunneling).
    
- **Connect WhatsApp to n8n via a Webhook.** In your UltraMsg (or Twilio) settings, configure the “Incoming Message” webhook URL to point to an n8n Webhook node. UltraMsg will POST each new message as JSON containing fields like `data.from` (customer number) and `data.body` (message text). In n8n, set up a **Webhook node** (e.g. at path `/whatsapp-webhook`) to catch these incoming messages.
    

From there, build the n8n workflow:

## 1. Set up WhatsApp API Provider

- **UltraMsg:** Create an account at UltraMsg and create a messaging instance. Sign in, scan the QR code with your phone’s WhatsApp to link it, and note the _Instance ID_ and _Token_. (Or use Twilio’s WhatsApp Sandbox by signing up for Twilio, enabling the Sandbox, and using the shared sandbox number.)
    
- **Configure Webhook:** In UltraMsg’s dashboard, go to **Settings → WebHooks** and set the “On Received Message” URL to your n8n Webhook endpoint (e.g. `https://<your-domain>/webhook/whatsapp-webhook`). UltraMsg will POST JSON like:
    
    `{   "event_type": "message_received",   "instanceId": "...",   "data": {     "from": "<customer_whatsapp_id>",     "to": "<your_whatsapp_id>",     "body": "<customer message text>",     // ... other fields ...   } }`
    
    For example, `data.from` contains the sender’s number and `data.body` the text.
    

## 2. Host n8n on a Free/Low-Cost VPS

Install n8n on a VPS (Docker is easiest). Many use **Oracle Cloud Free Tier** (free ARM VM) or AWS/Azure free credits. DigitalOcean has tutorials for installing n8n on Ubuntu/Docker. Once n8n is running, ensure it’s reachable (via domain or reverse proxy) so UltraMsg can reach your webhook.

## 3. Build the n8n Workflow

1. **Webhook Trigger:** Add an **HTTP Webhook** node in n8n. Set it to the path you gave UltraMsg (e.g. `/webhook/whatsapp-webhook`) and method POST. This node will receive incoming WhatsApp messages. The output will contain JSON under `{{$json["body"]["data"]}}`, e.g. `{{$json.body.data.from}}` (customer number) and `{{$json.body.data.body}}` (text).
    
2. **Store Conversation Context:** To maintain dialogue state, use n8n’s **Simple Memory** (or a database) keyed by user number. For example, add a **Function** or **Set** node to append the incoming message to a session history. You can store messages as an array of `{role: "user", content: "..."} and {role: "assistant", content: "..."} }`. n8n’s Memory node can store the last N messages per user. This ensures ChatGPT sees previous Q&A for context.
    
3. **AI Chat (OpenAI):** Add an **OpenAI Chat Model** node (or HTTP Request to OpenAI API). Set it to use e.g. `gpt-3.5-turbo`. Provide a **system prompt** that encodes the business logic. For example, the system prompt might say:
    
    `You are a helpful pupusa restaurant ordering assistant.  - Always greet the customer politely.  - Ask which pupusa types and quantities they want.  - Ask if they want pickup or delivery.  - Tell them delivery requires a minimum order of 150 MXN. If they choose delivery with less than 150 MXN, prompt them to add more or choose pickup.  - Ask for their address if needed (for delivery). Confirm directions clearly.  - Only accept cash payment; explicitly confirm they will pay in cash (no other payment methods).  - After gathering all details, give an order summary and confirm.`
    
    Then supply the accumulated conversation (from memory) plus the latest user message as the Chat completion input. The node will output the AI’s reply. n8n’s Chat Model node handles conversation lists; just feed it the JSON message list from memory. The AI will generate the next question or confirmation following those rules.
    
4. **Send Reply via WhatsApp:** After the AI node, add an **HTTP Request** node to send the AI’s reply back to the user via WhatsApp. Use the UltraMsg “send chat” API. Configure it like:
    
    - **Method:** POST
        
    - **URL:** `https://api.ultramsg.com/{{ $credentials.ultramsg.instance_id }}/messages/chat`
        
    - **Query/JSON Body:**
        
        `{   "token": "<Your_UltraMsg_Token>",   "to": "<{{$json.body.data.from}}>",   // the customer number   "body": "{{$node[\"OpenAI Chat\"].json[\"choices\"][0][\"message\"][\"content\"]}}" }`
        
    
    This sends the AI-generated message to the customer. In curl form, it’s:
    
    `curl -X POST "https://api.ultramsg.com/INSTANCE_ID/messages/chat" \   -d "token=YOUR_TOKEN" \   -d "to=+52XXXXXXXXXXX" \   -d "body=Your message here"`
    
    (UltraMsg’s API requires `token`, `to`, and `body` fields.)
    
5. **Order Completion & Notify Mom:** When the conversation finishes (e.g. after confirming all details), compile an order summary (items, quantities, total, address, payment method). Then send this summary as a _new WhatsApp message_ to your mom’s number. You can do this with another HTTP Request to UltraMsg:
    
    `{   "token": "<Your_Token>",   "to": "<+52MOM_NUMBER>",   "body": "📦 *New Order Received!* %0A%0A_Pupusa Order Summary:_ %0A- Item1 x2 %0A- Item2 x3 %0A*Total:* 180 MXN%0A*Pickup or Delivery:* Delivery%0A*Address:* 123 Main St, Zapopan%0A*Payment:* Cash" }`
    
    Example in code (URL-encoded newlines with `%0A`):
    
    `curl -X POST "https://api.ultramsg.com/INSTANCE_ID/messages/chat" \   -d "token=YOUR_TOKEN" \   -d "to=+52<MOM_NUMBER>" \   -d "body=📦 *Nuevo Pedido*%0A%0A- Pupusas de Queso x2%0A- Pupusas Revuelta x3%0A*Total:* 180 MXN%0A*Retiro/Delivery:* Delivery%0A*Dirección:* Calle Falsa 123, Zapopan%0A*Pago:* Efectivo"`
    
    This ensures your mom gets a formatted ticket via WhatsApp with all order details.
    
6. **Logic for Business Rules:** Incorporate logic checks if needed. For example, after AI replies, you could use an **If** node or a **Function** node to verify the answer: if the customer chose delivery but total<150 MXN, send a message “Minimum 150 MXN for delivery” (the AI prompt should already enforce this). Similarly, ensure you record that payment is “Cash”. The system prompt should drive the AI to only accept cash and confirm it.
    

## 4. Putting It All Together

The final workflow might look like:

- **Webhook (Incoming WhatsApp)** → **(Function/Memory) Store context** → **OpenAI Chat Model** → **HTTP Request (Send to customer)** → **(Function) Check if order is complete** → **HTTP Request (Send summary to mom)**.
    

This uses only n8n’s built-in nodes and UltraMsg’s API (free trial), plus OpenAI. The only costs are for (optional) OpenAI API calls and eventual UltraMsg subscription. However, with ~40 messages/week, GPT-3.5 usage is very low cost (fractions of a dollar) and UltraMsg provides a 3-day trial (or use Twilio Sandbox for free testing).

**References:** Official guides note that n8n can integrate with WhatsApp via providers like UltraMsg and that you use an HTTP Request node to call the provider’s API. UltraMsg’s documentation shows sending messages via POST with `token`, `to`, and `body` parameters. To manage conversation context, n8n’s memory feature or similar storage is used. Finally, n8n can leverage OpenAI’s language models for conversational AI, allowing dynamic Q&A (e.g. confirming address, payment, etc.) in your chat flow.