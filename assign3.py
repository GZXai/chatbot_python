from assign3_quotes import *
import random

#-----------------------------------------------------------
# Movie Quotes Analysis Section

def is_question(str):
    """
    判断字符串是否以？结尾
    :param str:
    :return:
    """
    if len(str)==0:
        return False
    return str[-1]=='?'#标号-1对于字符串的最后一个元素,返回一个布尔值的表达式

def get_first_quotes(quotes):
    """
    获取所有台词对中的第一句台词
    :param quotes:
    :return:
    """
    first_lines=[]
    for pair in quotes:#遍历列表每一个元素，每个元素是元组又能通过索引访问元组的元素
        first_lines.append(pair[0])#将每个台词对的第一句话添加到列表尾部
    return first_lines

def get_first_questions(quotes):
    """
    从所有第一句台词中筛选出问题
    :param quotes:
    :return:
    """
    all_first_lines = get_first_quotes(quotes)#获取所有第一句话
    questions=[]
    for quote in all_first_lines:
        if is_question(quote):
            questions.append(quote)
    return questions

def count_question_quotes(quotes):
    """
    统计作为问题的第一个台词数量
    :param quotes:
    :return:
    """
    all_questions=get_first_questions(quotes)
    return len(all_questions)

def get_average_question_length(quotes):
    """
    计算问题台词的平均长度
    :param quotes:
    :return:
    """
    all_questions=get_first_questions(quotes)

    # 如果没有问题台词，返回0避免除零错误
    if len(all_questions) == 0:
        return 0
    total=0
    for quote in all_questions:
        total+=len(quote)
    average = total/len(all_questions)
    return average

#-----------------------------------------------------------
# Chatbot Section

def get_responses(quotes,question):
    """
    根据问题查找所有可能的回答
    :param quotes:
    :param question:
    :return:
    """
    possible_answers=[]
    for pair in quotes:
        if pair[0]==question:
            possible_answers.append(pair[1])
    return possible_answers

def get_random_from_list(lst):
    """
    从列表中随机选择一个元素,用于从可能回答中随机选择一个
    :param lst:
    :return:
    """
    if len(lst)==0:
        return None
    random_index=random.randint(0,len(lst)-1)
    return lst[random_index]

def respond(quotes,question):
    """
    生成对问题的最终响应
    :param quotes:
    :param question:
    :return:
    """
    possible_answers=get_responses(quotes,question)
    if len(possible_answers)>0:
        return get_random_from_list(possible_answers)
    else:
        return "I don't know."

def chatbot():
    """
    主聊天机器人函数
    """
    print("Welcome to use chatbot！")
    print("You can ask me any questions, enter 'bye' to exit")
    # 加载所有台词数据
    all_quotes = get_quotes()#调用assign3_quotes.py中的函数

    while True:
        user_input=input("You: ").strip()
        if user_input.lower()=='bye':
            print("Bot: Bye！")
            break#只有用户输入bye才会停止循环
        lower=user_input.lower()
        if not is_question(lower):
            print("Bot: I only respond to questions!")
            continue#继续进入下一次循环（询问）
        answer = respond(all_quotes,lower)
        print(f"Bot: {answer}")


if __name__ == "__main__":
    # 加载真实台词数据
    movie_quotes = get_quotes()

    # 统计并显示问题台词数量
    question_count = count_question_quotes(movie_quotes)
    print(f"电影台词库中共有 {question_count} 个问句")

    # 启动聊天机器人
    chatbot()




