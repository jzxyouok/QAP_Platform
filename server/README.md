##数据服务接口
####1. login
用户登录

HTTP POST请求方式, 访问接口: http://127.0.0.1:10100/doUserAct/Login, 请求示例:

	curl -d "username=xxx&password=xxx" "http://127.0.0.1:10100/doUserAct"

请求参数格式说明:

	{
		"username": "flyfish",				// 登录用户名
		"password": "flyfish"				// 登录密码
	}

返回结果说明:
	
	{
		"code": 200,							// OK
		"data": {
			"username": "flyfish",			         // 用户名
			"card_number": "1111111111111",        // 证件号码
			"address": "xxx",			            // 家庭住址
			"grade": 1,                           // 年级
			"name": "flyfish",                    // 真实姓名
			"birthday": "2015-09-11",             // 生日
			"identifier": 0,                      // 身份标识
			"avatar_url": "/data/avatars/flyfish.png",	               // 头像索引
			"phone_number": "000000000000",       // 电话号码
			"sex": 0,                             // 性别
			"email": "flyfish@ifeiyu.net",        // 电子邮箱
			"access_token": "aej8emleui56ekwl",   // token串
			"ts": 1438874007					        // 时间戳（用于验证token是否过期）
	}

####2. register
用户注册

HTTP POST请求方式, 访问接口: http://127.0.0.1:10100/doUserAct/Register, 请求示例:

	curl -d "username=xxx&password=xxx&grade=xxx&user_type=xxx&serial_number=xxx&options={\"phone_number\": xxx, ...}" "http://127.0.0.1:10100/doUserAct/Register"

请求参数格式说明:

	{
		"username": "flyfish",				    // 注册用户名
		"password": "flyfish",			       // 注册密码
		"grade": 1,							   //  注册年级(0: 小学 1: 初中 2: 高中)
		"identifier": 0,				          // 用户身份类别 (0: 学生 1: 教师)
		"serial_number": 1103710520,		   // 教师工作证号(学生注册不填写)
		"options": {"phone_number": 15145102540, ....}    // 选填信息(Json序列串, 注意格式)
	}
	
返回结果说明:

	{
		"code": 200,							// OK, 其余状态码均失败
		"data": {
			"msg": "注册成功"
		}
	}

####3. QueryQuestionList
请求问题列表

HTTP POST请求方式, 访问接口: http://127.0.0.1:10100/doQuestionAct/QueryQuestionList, 请求示例:
	
	curl -d "username=xxx" "http://127.0.0.1:10100/doQuestionAct/QueryQuestionList"

请求参数格式说明:
	
	{
		"username": "flyfish"		         // 用户名
	}
	
返回结果说明:
	
	{
		"code": 200,						      // OK
		"data": [
			{
				"question_username": "flyfish",                // 提问者
				"avatar_url": "/data/avatars/flyfish.png",     // 头像索引
				"question_grade": 1,		                    // 问题对应的年级
				"question_subject": 2,                        // 问题所属科目
				"question_head" "xxx",                        // 系统随机注入的信息头部 
				"quetion_content": "xxx",                     // 问题内容
				"question_score": 10,                         // 问题悬赏积分
				"answer_counts": 3,                           //  问题回答的数目
				"question_time": "2015-08-10 00:13:13"        // 提问时间
			},
			......
		]
	}


####4. PostQuestion
用户提问

HTTP POST请求方式, 访问接口: http://127.0.0.1:10100/doQuestionAct/PostQuestion, 请求示例:

	curl -d "username=xxx&grade=xxx&subject=xxx&content_type=xxx&question_content=xxx&question_score=xxx" "http://127.0.0.1:10100/doQuestionAct/PostQuestion"

请求参数格式说明:

	{
		"username": "flyfish",			                // 用户名
		"grade": 1,							            // 年级
		"subject": 2,                                // 科目
		"content_type": 0, 				               // 问题内容类型
		"question_content": "xxx",                   // 问题内容
		"question_score": 10			               // 问题悬赏积分
	}
	
返回结果说明:
	
	{
		"code": 200,						    // OK
		"data": {
			"msg": "提问成功"
		}
	}


####5. ConnectQuestion
收藏问题

HTTP POST请求方式, 访问接口: http://127.0.0.1:10100/doQuestionAct/ConnectQuestion, 请求示例:

	curl -d "username=xxx&question_id=xxx" "http://127.0.0.1:10100/doQuestionAct/ConnectQuestion"

请求参数格式说明:

	{
		"username": "flyfish",                  // 用户名
		"question_id": 1001				          // 问题ID
	}
	
返回结果说明:

	{
		"code": 200,						   // Ok
		"data": {
			"msg": "收藏成功"
		}
	}


####6. SearchQuestion
用户搜索问题

HTTP POST请求方式, 访问接口: http://127.0.0.1:10100/doQuestionAct/SearchQuestion, 请求示例:

 	curl -d "username=xxx&question_content=xxx" "http://127.0.0.1:10100/doQuestionAct/SearchQuestion"
 
 请求参数格式说明:
 
 	{
 		"username": "flyfish",                      // 用户名
 		"question_content": "xxx"	                 // 查询的问题内容
 	}
 
 返回结果说明:
 
	 {
	 	"code": 200,						      // OK
		"data": [
			{
				"question_username": "flyfish",                // 提问者
				"avatar_url": "/data/avatars/flyfish.png",     // 头像索引
					"question_grade": 1,		                    // 问题对应的年级
					"question_subject": 2,                        // 问题所属科目
					"question_head" "xxx",                        // 系统随机注入的信息头部 
					"quetion_content": "xxx",                     // 问题内容
					"question_score": 10,                         // 问题悬赏积分
					"answer_counts": 3,                           //  问题回答的数目
					"question_time": "2015-08-10 00:13:13"        // 提问时间
				},
				......
			]
	 }
	
####7. AnswerQuestion
回答问题

HTTP POST请求方式, 访问接口: http://127.0.0.1:10100/doQuestionAct/AnswerQuestion, 请求示例:

	curl -d "username=xxx&question_id=xxx&content_type=xxx&answer_content=xxx" "http://127.0.0.1:10100/doQuestionAct/AnswerQuestion"

请求参数格式说明:

	{
		"username": "flyfish",                     // 用户名
		"question_id": 1001,		                // 回答的问题ID
		"content_type": 0,					         // 回答内容的类型
		"answer_content": "xxx"                   // 回答的内容
	}

返回结果说明:

	{
		"code": 200,                             // OK
      	"data": {
           "msg": "回答成功"
       }
	}

####8. AskQuestion
用户追问

HTTTP POST请求方式, 访问接口: http://127.0.0.1:10100/doQuestionAct/AskQuestion, 请求示例:

	curl -d "username=xxx&content_type=xxx&ask_content=xxx&original_quetion_id=xxx&be_asked_username=xxx" "http://127.0.0.1:10100/doQuestionAct/AskQuestion"


请求参数格式说明:

	{
		"username": "flyfish",                       // 追问者的用户名
		"content_type": 0,					           // 追问内容类型
		"ask_content": "xxx",                       // 追问内容
		"original_question_id": 1001,               // 原问题的ID
		"be_asked_username": "flyfish"              // 被追问者的用户名
	}

返回结果说明:

	{
		"code": 200,			                       // OK
		"data": {
			"msg": "追问成功"
		}
	}


####9. QueryUserQuestionDetail
请求问题详细信息

HTTP POST请求方式, 访问接口: http://127.0.0.1:10100/doQuestionAct/QueryUserQuestionDetail, 请求示例:

	curl -d "username=xxx&question_id=xxx" "http://127.0.0.1:10100/doQuestionAct/QueryUserQuestionDetail"

请求参数格式说明:

	{
		"username": "flyfish",                   // 用户名
		"question_id": 1001                      // 问题ID
	}
	
返回结果说明:

	{
		"code": 200,				           // OK
		"data": {
			"question_info": {
				"question_username": "flyfish",                // 提问者
				"avatar_url": "/data/avatars/flyfish.png",     // 头像索引
				"question_grade": 1,		                    // 问题对应的年级
				"question_subject": 2,                        // 问题所属科目
				"question_head" "xxx",                        // 系统随机注入的信息头部 
				"quetion_content": "xxx",                     // 问题内容
				"question_score": 10,                         // 问题悬赏积分
				"answer_counts": 3,                           //  问题回答的数目
				"question_time": "2015-08-10 00:13:13"        // 提问时间
			},
			"answers_info": [{
				"answer_username": "flyfish",                // 回答者
				"avatar_url": "/data/avatars/flyfish.png",     // 头像索引 
				"answer_content": "xxx",                     // 回答内容
				"is_accepted": 0,			                  // 是否被采纳
				"answer_time": "2015-08-10 00:13:13"        // 回答的最新时间
			},
			......  
			]
		}
	}

####10. SignDaily
每日签到

HTTP POST请求, 访问接口: http://127.0.0.1:10100/doUserAct/SignDaily, 请求示例:

	curl -d "username=xxx" "http://127.0.0.1:10100/doUserAct/SignDaily"

请求参数格式说明:

	{
		"username": "flyfish"	                     // 用户名
	}
	
返回结果说明:

	{
		"code": 200,		                 // OK
		"data": {
			"msg": "签到成功"
		}
	}

####11. QueryUserPointsDetail
请求用户积分明细

HTTP POST请求, 访问接口: http://127.0.0.1:10100/doUserAct/QueryUserPointsDetail, 请求示例:

	curl -d "username=xxx" "http://127.0.0.1:10100/doUserAct/QueryUserPointsDetail"
	
请求参数格式说明:

	{
		"username": "flyfish"                 // 用户名
	}

返回结果说明:

	{
		"code": 200,	                       // OK
		"data": {
			"total_points": 200,             // 总积分
			"point_detail":[
			 {
				"point_type": 1,             // 积分类型
				"point_desc": "xxx",         // 类型描述
				"point_value": 20            // 单项积分
			 },
			 ......
		  ]
		}
	}
	
####12. FollowOther
关注其他用户

HTTP POST请求方式, 访问接口: http://127.0.0.1:10100/doUserAct/FollowOther, 请求示例:

	curl -d "username=xxx&other_name=xxx" "http://127.0.0.1:10100/doUserAct/FollowOther"

请求参数格式说明:

	{
		"username": "flyfish",                  // 用户名
		"other_name": "flyfish13"               // 其他用户
	}

返回结果说明:

	{
		"code": 200,                   // OK
		"data": {
			"msg": "关注成功"
		}
	}

####13. QueryFollowers
请求关注/粉丝列表

HTTP POST请求方式, 请求接口: http://127.0.0.1:10100/doUserAct/QueryFollowers, 请求示例:

	curl -d "username=xxx" "http://127.0.0.1:10100/doUserAct/QueryFollowers"
	
请求参数格式说明:

	{
		"username": "flyfish"                 // 用户名
	}

返回结果说明:

	{
		"code": 200,                         // OK
		"data": [
			{
				"username": "flyfish",                         // 用户名
				"avatar_index": "/data/avatars/flyfish.png",   // 头像索引
				"level_value": 1,                              // 等级
				"level_desc": "xxx"                            // 称号
			},
			......
		]
	}

####14. QueryUserQuestionsOrAnswers
请求用户的提问/回答列表

HTTP POST请求方式, 访问接口: http://127.0.0.1:10100/doUserAct/QueryUserQuestionsOrAnswers, 请求示例:

	curl -d "username=xxx" "http://127.0.0.1:10100/doUserAct/QueryUserQuestionsOrAnswers"
	
请求参数格式说明:

	{
		"username": "flyfish"                // 用户名
	}

1.学生

返回结果说明:

	{
		"code": 200,	                      // OK
		"data": {
			"question_counts": 200,        // 提问总数
			"complete_counts": 100         // 完成数
		}
	}

2.教师

返回结果说明:

	{
		"code": 200,                     // OK
		"data": {
			"answer_counts": 200,        // 回答总数
			"accepted_counts": 100       // 采纳数
		}
	}
	
####15 QueryUserConnectionQuestionList
请求用户收藏问题列表

HTTP POST请求方式, 访问接口: http://127.0.0.1:10100/doUserAct/QueryUserConnectionQuestionList, 请求示例: 

	curl -d "username=xxx" "http://127.0.0.1:10100/doUserAct/QueryUserConnectionQuestionList"
	
请求参数格式说明:
	{
		"username": "flyfish"               // 用户名
	}

返回结果说明:

	{
		"code": 200,	                 // OK
		"data": [
			{
				"question_id": 1001,               // 问题ID
				"question_content": "xxx"          // 问题内容
			},
			......
		]
	}