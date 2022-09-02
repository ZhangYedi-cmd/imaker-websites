import React from 'react';
import { QuestionType } from '@/models/question';
import { Col, Divider, List, Row, Space, Tag, Typography } from 'antd';
import { Link } from 'umi';
import { QUESTION_DIFFICULTY_ENUM, QUESTION_TYPE_ENUM } from '@/constant/question';

const { Title, Paragraph } = Typography;

interface QuestionItemProps {
  question: QuestionType;
  showReview?: boolean; // 显示审核状态
  showEdit?: boolean; // 显示修改
  showActions?: boolean; // 展示操作栏
  showReference?: boolean; // 展示解析
  onReload?: () => void;
  pickAble?: boolean;
  showOrder?: boolean; // 是否展示序号
  index?: number;
  target?: string;
}

const QuestionItem: React.FC<QuestionItemProps> = (props) => {
  const { question = {} as QuestionType } = props;

  return (
    <>
      <List.Item>
        <Link to={`/qd/${question._id}`}>
          <Title
            level={5}
            ellipsis={{ rows: 2 }}
            style={{ marginBottom: 16 }}
            className="question-item-title"
          >
            {question.name}
          </Title>
        </Link>
        <Row style={{ marginBottom: '2vh' }}>
          <Col>
            {question.tags.map((tag) => {
              return (
                <>
                  <Tag key={tag}>
                    <Link to={`/tag/${tag}`}>{tag}</Link>
                  </Tag>
                </>
              );
            })}
          </Col>
        </Row>

        <Row style={{ marginBottom: '1vh' }}>
          <Space split={<Divider type="vertical" />}>
            <span>{QUESTION_TYPE_ENUM[question?.type ?? 0]}题</span>
            <span>{QUESTION_DIFFICULTY_ENUM[question.difficulty ?? 0]}</span>
          </Space>
        </Row>
      </List.Item>
    </>
  );
};

export default QuestionItem;
