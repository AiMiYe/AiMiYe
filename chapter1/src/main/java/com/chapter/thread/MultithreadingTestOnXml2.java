package com.chapter.thread;

import org.testng.annotations.Test;

public class MultithreadingTestOnXml2 {
    @Test
    public void testMultithreading1(){
        System.out.println(4 + 4 + " 线程ID: " + Thread.currentThread().getId());
    }
    @Test
    public void testMultithreading2(){
        System.out.println(5 + 5 + " 线程ID: " + Thread.currentThread().getId());
    }
    @Test
    public void testMultithreading3(){
        System.out.println(6 + 6 + " 线程ID: " + Thread.currentThread().getId());
    }
}
