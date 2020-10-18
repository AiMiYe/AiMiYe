package com.course.server;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class GetMethods {
    @RequestMapping(value = "/massage",method = RequestMethod.GET)
    @ResponseBody
    public String getMassage(){
        return "获取信息成功!";
    }
}
