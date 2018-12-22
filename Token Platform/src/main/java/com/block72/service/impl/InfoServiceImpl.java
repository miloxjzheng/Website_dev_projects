package com.block72.service.impl;

import com.block72.mapper.ContactMapper;
import com.block72.mapper.SubscribeMapper;
import com.block72.model.Contact;
import com.block72.model.Subscriber;
import com.block72.service.InfoService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import tk.mybatis.mapper.entity.Example;
import tk.mybatis.mapper.util.Sqls;

import java.sql.Timestamp;
import java.util.List;

/**
 * Created by Jiateng on 11/1/18.
 */
@Service
public class InfoServiceImpl implements InfoService {

    @Autowired
    private SubscribeMapper subscribeMapper;
    @Autowired
    private ContactMapper contactMapper;

    @Override
    public Subscriber subscribe(Subscriber subscriber) {
        subscriber.setCreateTime(new Timestamp(System.currentTimeMillis()));
        subscriber.setUpdateTime(new Timestamp(System.currentTimeMillis()));
        int res = subscribeMapper.insert(subscriber);

        return res == 1 ? subscriber : null;
    }

    @Override
    public Subscriber getSubscriberById(long id) {
        return subscribeMapper.selectByPrimaryKey(id);
    }

    @Override
    public Subscriber getSubscriberByName(String firstName, String lastName) {
        Example example = Example.builder(Subscriber.class).
                where(Sqls.custom().
                        andEqualTo("first_name", firstName).
                        andEqualTo("last_name", lastName)).build();
        List<Subscriber> subscribers = subscribeMapper.selectByExample(example);
        return subscribers.size() == 0 ? null : subscribers.get(0);
    }

    @Override
    public Subscriber getSubscriberByEmail(String email) {
        Example example = Example.builder(Subscriber.class).
                where(Sqls.custom().
                        andEqualTo("email", email)).build();
        List<Subscriber> subscribers = subscribeMapper.selectByExample(example);
        return subscribers.size() == 0 ? null : subscribers.get(0);
    }

    @Override
    public Contact insertContactInfo(Contact contact) {
        contact.setCreateTime(new Timestamp(System.currentTimeMillis()));
        contact.setUpdateTime(new Timestamp(System.currentTimeMillis()));
        int res = contactMapper.insert(contact);

        return res == 1 ? contact : null;
    }
}
