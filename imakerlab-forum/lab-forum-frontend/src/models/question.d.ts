/**
 * 题目类型
 */
export interface QuestionType {
  _id?: string;
  name?: string;
  detail?: string;
  tags: string[];
  type?: number;
  difficulty?: number;
}
