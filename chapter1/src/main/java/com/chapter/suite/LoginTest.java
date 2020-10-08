package com.chapter.suite;

import org.testng.annotations.Test;

public class LoginTest {
    @Test
    public void loginSuccessful(){
        System.out.println("登陆成功~~~");
    }
    @Test
    public void loginFail(){
        System.out.println("登陆失败~~~");
    }
}
