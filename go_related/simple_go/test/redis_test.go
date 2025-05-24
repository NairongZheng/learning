// redis没有经过测试，这边就是给个大概的例子
package test

import (
	"context"
	"fmt"
	"testing"
	"time"

	"github.com/nairongzheng/simple_go/pkg/redisc"
	"github.com/redis/go-redis/v9"
	"github.com/stretchr/testify/assert"
)

var testClient = redis.NewClient(&redis.Options{
	Addr: "localhost:6379",
	DB:   15, // 使用测试专用数据库
})

func TestRedisCache_BasicOperations(t *testing.T) {
	ctx := context.Background()
	rc := redisc.NewRedisCache(testClient, ctx)

	// 清除测试数据
	testClient.FlushDB(ctx)

	fmt.Println("▶ 设置缓存")
	userData := struct {
		ID   int    `json:"id"`
		Name string `json:"name"`
		Age  int    `json:"age"`
	}{1, "Alice", 25}

	key := "user:1"
	item := redisc.NewItem(key, userData, 10*time.Second)

	err := rc.Set(item)
	if err != nil {
		t.Fatalf("设置缓存失败: %v", err)
	}

	fmt.Println("▶ 获取缓存")
	var result struct {
		ID   int    `json:"id"`
		Name string `json:"name"`
		Age  int    `json:"age"`
	}

	err = rc.Get(key, &result)
	if err != nil {
		t.Fatalf("获取缓存失败: %v", err)
	}

	fmt.Printf("缓存值：%+v\n", result)
	assert.Equal(t, userData, result, "缓存值不匹配")

	// 测试TTL
	ttl, err := rc.TTL(key)
	if err != nil {
		t.Fatalf("获取TTL失败: %v", err)
	}
	fmt.Printf("▶ TTL 剩余：%d 秒\n", int(ttl.Seconds()))
	assert.InDelta(t, 10, ttl.Seconds(), 1, "TTL不匹配")

	fmt.Println("▶ 等待缓存过期...")
	time.Sleep(11 * time.Second)

	err = rc.Get(key, &result)
	if err != redisc.ErrCacheMiss {
		t.Fatalf("缓存过期后应返回 ErrCacheMiss，实际返回: %v", err)
	}

	fmt.Println("缓存过期后获取失败：ErrCacheMiss")
}
