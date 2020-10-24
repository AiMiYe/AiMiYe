//package com.course.server.config;
//
//import org.springframework.context.annotation.Bean;
//import org.springframework.context.annotation.Configuration;
//import springfox.documentation.builders.ApiInfoBuilder;
//import springfox.documentation.builders.PathSelectors;
//import springfox.documentation.service.ApiInfo;
//import springfox.documentation.service.Contact;
//import springfox.documentation.spi.DocumentationType;
//import springfox.documentation.spring.web.plugins.Docket;
//import springfox.documentation.swagger2.annotations.EnableSwagger2;
//
//@Configuration
//@EnableSwagger2
//public class SwaggerConfig {
//    @Bean
//    public Docket api() {
//        return new Docket(DocumentationType.SWAGGER_2).apiInfo(apiInfo())
//                .pathMapping("/").select().paths(PathSelectors.regex("/.*")).build();
//    }
//
//    private ApiInfo apiInfo() {
//        return new ApiInfoBuilder().title("Course api").contact(
//                new Contact("532811131","","532811131@qq.com")
//        ).description("课程示例!").version("0.0.1").build();
//    }
//}
