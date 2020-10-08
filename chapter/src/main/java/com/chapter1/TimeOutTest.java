package com.chapter1;

import org.testng.annotations.Test;

public class TimeOutTest {
    @Test(timeOut = 3000)
    public void testSuccessful() {
        try {
            Thread.sleep(2000);
            System.out.println(1 + 1);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
    @Test(timeOut = 3000)
    public void testFail(){
        try {
            Thread.sleep(3001);
            System.out.println(2 + 2);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
