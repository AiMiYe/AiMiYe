package com.course.server;

import org.springframework.web.bind.annotation.*;

import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServletResponse;
import java.time.LocalDateTime;
import java.util.HashMap;

@RestController
public class PostMethods {

    // 实现post请求
    @RequestMapping(value = "/login", method = RequestMethod.POST)
    @ResponseBody
    public HashMap<String, String> login(HttpServletResponse response,
                                         @RequestParam(name = "username") String username,
                                         @RequestParam(name = "password") String password) {
        HashMap<String, String> map = new HashMap<>();
        if (username.equals("admin") && password.equals("admin")) {
            Cookie cookie = new Cookie("isLogin", "true");
            response.addCookie(cookie);
            map.put("code", "0");
            map.put("username", "admin");
            map.put("message", "登陆成功");
            map.put("loginTime", LocalDateTime.now().toString());
            map.put("token", "20201019215555");
        } else {
            map.put("code", "-1");
            map.put("message", "用户名或密码错误,请重新登陆.");
            map.put("loginTime", LocalDateTime.now().toString());
        }
        return map;
    }
}
