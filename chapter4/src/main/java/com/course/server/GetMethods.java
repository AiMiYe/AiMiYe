package com.course.server;

import com.alibaba.fastjson.JSONObject;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.util.Objects;

@RestController
@RequestMapping(value = "/get")
public class GetMethods {
    // HttpServletResponse: 存放响应信息的类
    // HttpServletRequest: 存放请求信息的类
    // 实现get请求的接口
    @RequestMapping(value = "/massage", method = RequestMethod.GET)
    @ResponseBody
    public String getMassage(HttpServletResponse servletResponse) {
        // 设置cookie
        Cookie cookie = new Cookie("isLogin", "true");
        servletResponse.addCookie(cookie);
        return "获取信息成功!";
    }

    // 实现需要携带cookie信息的接口
    @RequestMapping(value = "/getuser", method = RequestMethod.GET)
    @ResponseBody
    public String getUser(HttpServletRequest request) {
        Cookie[] cookies = request.getCookies();
        if (Objects.isNull(cookies)) {
            return "请求失败, 无Cookies信息.";
        }
        for (Cookie cookie : cookies) {
            if (cookie.getName().equals("isLogin") && cookie.getValue().equals("true")) {
                return "请求成功.";
            }
        }
        return "请求失败, 无Cookies信息.";
    }

    // 实现一个需要传入参数的get请求
    @RequestMapping(value = "/getparams", method = RequestMethod.GET)
    @ResponseBody
    public String getParams(@RequestParam(name = "username", required = true) String username) {
        JSONObject jsonObject = new JSONObject();
        jsonObject.put("username", "Alice");
        jsonObject.put("sex", "女");
        jsonObject.put("addr", "中国四川成都");
        jsonObject.put("手机号", "15328462548");
        jsonObject.put("age", "24");

        if (username.equals("Alice")) {
            return jsonObject.toJSONString();
        }
        return "你输入的用户名不存在";
    }


}
