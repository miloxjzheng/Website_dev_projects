package com.block72.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;


/**
 * Views
 * Created by Jiateng on 10/19/18.
 */
@Controller
public class MainController {

    @GetMapping("/")
    public String index() {
        return "homepage";
    }

    @GetMapping("/contact")
    public String contact() {
        return "contactpage";
    }

    @GetMapping("/subscribe")
    public String subscribe() {
        return "subscribepage";
    }

    @GetMapping("/policy")
    public String policy() {
        return "privacypolicypage";
    }

    @GetMapping("/team")
    public String team() {
        return "team";
    }

    @GetMapping("/tofservice")
    public String tofservice() {
        return "tofservice";
    }

}
