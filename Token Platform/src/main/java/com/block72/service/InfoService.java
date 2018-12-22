package com.block72.service;

import com.block72.model.Contact;
import com.block72.model.Subscriber;

/**
 * Created by Jiateng on 11/1/18.
 */
public interface InfoService {

    /**
     * Do subscription
     *
     * @param subscriber
     * @return null if fail
     */
    Subscriber subscribe(Subscriber subscriber);

    /**
     * @param id
     * @return null if doesn't exist
     */
    Subscriber getSubscriberById(long id);

    /**
     * @param id
     * @return null if doesn't exist
     */
    Subscriber getSubscriberByName(String firstName, String lastName);

    /**
     * @param id
     * @return null if doesn't exist
     */
    Subscriber getSubscriberByEmail(String email);

    /**
     *
     * @param contact
     * @return null if fail
     */
    Contact insertContactInfo(Contact contact);
}
