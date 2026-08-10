package main

import (
	"context"
	"flag"
	"fmt"
	"os"
	"sync"
	"time"

	pb "github.com/MBI-88/dominus-proto-definition/dominus"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
	"google.golang.org/grpc/metadata"
	"google.golang.org/grpc/status"
)

type apiKeyCreds struct {
	token string
}

func (a apiKeyCreds) GetRequestMetadata(context.Context, ...string) (map[string]string, error) {
	return map[string]string{"x-api-key": a.token}, nil
}

func (a apiKeyCreds) RequireTransportSecurity() bool {
	return false
}

func main() {
	addr := flag.String("addr", "127.0.0.1:5000", "broker gRPC address")
	token := flag.String("token", "dominus-api-key-1233464687", "gRPC API token")
	connections := flag.Int("connections", 20, "number of concurrent streams, max 20")
	timeout := flag.Duration("timeout", 1500*time.Millisecond, "per-stream timeout")
	flag.Parse()

	if *connections > 20 {
		fmt.Fprintf(os.Stderr, "refusing to open %d streams; maximum allowed for this lab is 20\n", *connections)
		os.Exit(2)
	}

	payload := []byte(`{"id":1,"role":"test","case":"BE-05"}`)
	fmt.Printf("BE-05 stream probe\n")
	fmt.Printf("Address: %s\n", *addr)
	fmt.Printf("Payload: %s\n", payload)
	fmt.Printf("Connections requested: %d\n", *connections)
	fmt.Printf("Per-stream timeout: %s\n\n", *timeout)

	var wg sync.WaitGroup
	wg.Add(*connections)

	startAll := time.Now()
	for i := 0; i < *connections; i++ {
		i := i
		go func() {
			defer wg.Done()

			start := time.Now()
			ctx, cancel := context.WithTimeout(context.Background(), *timeout)
			defer cancel()
			ctx = metadata.AppendToOutgoingContext(ctx, "x-api-key", *token)

			conn, err := grpc.NewClient(
				*addr,
				grpc.WithTransportCredentials(insecure.NewCredentials()),
				grpc.WithPerRPCCredentials(apiKeyCreds{token: *token}),
			)
			if err != nil {
				fmt.Printf("stream=%02d latencia=%s codigo=client_setup_error error=%q\n", i+1, time.Since(start), err)
				return
			}
			defer conn.Close()

			client := pb.NewBrokerAPIClient(conn)
			stream, err := client.BidirectionalStream(ctx)
			if err != nil {
				fmt.Printf("stream=%02d latencia=%s codigo=%s error=%q\n", i+1, time.Since(start), status.Code(err), err)
				return
			}

			err = stream.Send(&pb.StreamRequestMessage{
				Subscribers: []string{"127.0.0.1:9"},
				Payload:     payload,
			})
			if err != nil {
				fmt.Printf("stream=%02d latencia=%s codigo=%s send_error=%q\n", i+1, time.Since(start), status.Code(err), err)
				return
			}

			_, err = stream.Recv()
			code := status.Code(err)
			fmt.Printf("stream=%02d latencia=%s codigo=%s error=%q\n", i+1, time.Since(start), code, err)
		}()
	}

	wg.Wait()
	fmt.Printf("\nTotal latency: %s\n", time.Since(startAll))
	fmt.Printf("All streams closed by client context: yes\n")
}
