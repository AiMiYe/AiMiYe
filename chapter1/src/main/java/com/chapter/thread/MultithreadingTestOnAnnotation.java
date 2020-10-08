package com.chapter.thread;

import org.testng.annotations.Test;

public class MultithreadingTestOnAnnotation {
    @Test(invocationCount = 15, threadPoolSize = 5) // 该注解表示使用多线程执行该测试用例. 注意需要指定线程数大小以及线程池大小
    public void testMultithreading(){
        System.out.println(1 + 1 + " 线程ID: " + Thread.currentThread().getId());
    }
}
