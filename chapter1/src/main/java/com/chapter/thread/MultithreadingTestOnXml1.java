package com.chapter.thread;

import org.testng.annotations.Test;

public class MultithreadingTestOnXml1 {
    @Test
    public void testMultithreading1(){
        System.out.println(1 + 1 + " 线程ID: " + Thread.currentThread().getId());
    }
    @Test
    public void testMultithreading2(){
        System.out.println(2 + 2 + " 线程ID: " + Thread.currentThread().getId());
    }
    @Test
    public void testMultithreading3(){
        System.out.println(3 + 3 + " 线程ID: " + Thread.currentThread().getId());
    }
}
