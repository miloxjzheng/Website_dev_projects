package com.block72.controller.api;

import com.block72.common.ErrorCode;
import com.block72.common.JsonResponse;
import com.block72.common.ServiceException;
import com.block72.model.Contact;
import com.block72.model.Subscriber;
import com.block72.service.InfoService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

/**
 * Created by Jiateng on 11/1/18.
 */
@RestController

public class InfoController {

    @Autowired
    private InfoService infoService;

    @PostMapping
    @CrossOrigin
    @RequestMapping(value = "/api/subscribe", produces = "application/json")
    public JsonResponse subscribe(@RequestBody Subscriber subscriber) throws ServiceException {
        if (infoService.getSubscriberByEmail(subscriber.getEmail()) != null)
            throw new ServiceException(ErrorCode.FAIL.getCode(), "Email = " + subscriber.getEmail() + "exists");
        subscriber = infoService.subscribe(subscriber);
        return new JsonResponse(subscriber);
    }

    @PostMapping
    @CrossOrigin
    @RequestMapping(value = "/api/contact", produces = "application/json")
    public JsonResponse contact(@RequestBody Contact contact) throws ServiceException {
        contact = infoService.insertContactInfo(contact);
        return new JsonResponse(contact);
    }

}
