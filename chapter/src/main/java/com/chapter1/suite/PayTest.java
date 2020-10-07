package com.chapter1.suite;

import org.testng.annotations.Test;

public class PayTest {
    @Test
    public void paySuccessful(){
        System.out.println("支付成功~~~");
    }
    @Test
    public void payFail(){
        System.out.println("支付失败~~~");
    }
}
