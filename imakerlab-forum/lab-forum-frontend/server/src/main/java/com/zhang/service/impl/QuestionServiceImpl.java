package com.zhang.service.impl;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.zhang.model.entity.Question;
import com.zhang.mapper.QuestionMapper;
import com.zhang.service.QuestionService;
import org.springframework.stereotype.Service;

/**
* @author yedizhang
*/
@Service
public class QuestionServiceImpl extends ServiceImpl<QuestionMapper, Question>
    implements QuestionService{

}




