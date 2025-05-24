package redisc

import (
	"context"
	"errors"
	"fmt"
	"time"

	redis "github.com/redis/go-redis/v9"
)

// 自定义缓存未命中错误
var ErrCacheMiss = errors.New("cache miss")

type RedisCache struct {
	client *redis.Client
	ctx    context.Context
}

func (rc *RedisCache) set(item *Item) error {
	bytes, err := Marshal(item.Value())
	if err != nil {
		return err
	}
	return rc.client.Set(rc.ctx, item.Key(), bytes, item.TTL()).Err()
}

func (rc *RedisCache) get(key string, target interface{}) error {
	result, err := rc.client.Get(rc.ctx, key).Result()
	if err != nil {
		if err == redis.Nil {
			return ErrCacheMiss
		}
		return err
	}
	if err := Unmarshal([]byte(result), target); err != nil {
		return fmt.Errorf("unmarshal: %w", err)
	}
	return nil
}

func (rc *RedisCache) Set(item *Item) error {
	return rc.set(item)
}

func (rc *RedisCache) SetString(item *Item) error {
	value, ok := item.Value().(string)
	if !ok {
		return fmt.Errorf("value is not a string")
	}
	return rc.client.Set(rc.ctx, item.Key(), value, item.TTL()).Err()
}

func (rc *RedisCache) SetInt(item *Item) error {
	value, ok := item.Value().(int)
	if !ok {
		return fmt.Errorf("value is not an int")
	}
	return rc.client.Set(rc.ctx, item.Key(), value, item.TTL()).Err()
}

func (rc *RedisCache) Get(key string, value interface{}) error {
	return rc.get(key, value)
}

func (rc *RedisCache) GetString(key string, value *string) error {
	result, err := rc.client.Get(rc.ctx, key).Result()
	if err != nil {
		if err == redis.Nil {
			return ErrCacheMiss
		}
		return err
	}
	*value = result
	return nil
}

func (rc *RedisCache) GetInt(key string, value *int) error {
	result, err := rc.client.Get(rc.ctx, key).Int()
	if err != nil {
		if err == redis.Nil {
			return ErrCacheMiss
		}
		return err
	}
	*value = result
	return nil
}

func (rc *RedisCache) Delete(key string) error {
	return rc.client.Del(rc.ctx, key).Err()
}

func (rc *RedisCache) TTL(key string) (time.Duration, error) {
	dur, err := rc.client.TTL(rc.ctx, key).Result()
	if err != nil {
		return 0, err
	}
	// 处理键不存在的情况
	if dur < 0 {
		return 0, ErrCacheMiss
	}
	return dur, nil
}

// NewRedisCache 创建一个新的 Redis 缓存实例
func NewRedisCache(client *redis.Client, ctx context.Context) *RedisCache {
	return &RedisCache{
		client: client,
		ctx:    ctx,
	}
}
