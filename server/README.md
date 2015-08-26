##数据服务接口
###1 login
用户登录

HTTP POST请求方式, 访问接口: http://123.59.71.144:10100/doUserAct/Login, 请求示例:

	curl -d "username=xxx&password=xxx&&identifier=xxx" "http://123.59.71.144:10100/doUserAct/Login"

请求参数格式说明:

	{
		"username": "flyfish@ifeiyu.net",				// 登录用户名
		"password": "flyfish",				            // 登录密码
		"identifier": 0                              // 身份标识 (0: 学生 1: 教师)
	}

1.登录成功

返回结果说明:

	{
		"code": 200,							// OK
		"data": {
			"username": "flyfish@ifeiyu.net",			         // 用户名
			"nickname": "fishzz",                   // 昵称
			"has_sign_today": 0,                    // 是否已签到 (1: 是 0: 否)
			"card_number": "1111111111111",        // 证件号码
			"address": "xxx",			            // 家庭住址
			"grade": 1,                           // 年级(1: 小学 2: 初中 3: 高中)
			"subject": 2,                         // 科目(1: 数学 2: 语文 3: 英语 4: 生物 5: 政治 6: 历史 7: 地理 8: 物理 9: 化学)
			"serial_number": "12345678",          // 工作证号(暂定为8位数字)
			"name": "flyfish",                    // 真实姓名
			"birthday": "2015-09-11",             // 生日
			"identifier": 0,                      // 身份标识(0: 学生 1: 教师)
			"avatar_url": "/data/avatars/flyfish.png",	               // 头像索引
			"phone_number": "000000000000",       // 电话号码
			"sex": 0,                             // 性别(0: 男 1: 女)
			"access_token": "aej8emleui56ekwl",   // token串
			"ts": 1438874007					        // 时间戳（用于验证token是否过期）
		}，
		"msg": ""
	}
2.登录失败

返回结果说明:

	{
		"code": 201,							       // FAIL
		"msg": "用户名或密码错误"
	}

###2 register
用户注册

HTTP POST请求方式, 访问接口: http://123.59.71.144:10100/doUserAct/Register, 请求示例:

	curl -d "username=xxx&password=xxx&grade=xxx&identifier=xxx&nickname=xxx&options={\"phone_number\": xxx, ...}" "http://123.59.71.144:10100/doUserAct/Register"

1.学生注册

请求参数格式说明:

	{
		"username": "flyfish@ifeiyu.net",				    // 注册用户名
		"password": "flyfish",			       // 注册密码
		"grade": 1,							   //  注册年级(1: 小学 2: 初中 3: 高中)
		"identifier": 0,				          // 用户身份类别 (0: 学生 1: 教师)
		"nickname": "cls1991",              // 昵称
		"options": "{\"phone_number\": \"15145102540\", ....}"    // 选填信息
	}

返回结果说明:

	{
		"code": 200,							// OK, 其余状态码均失败
		"data": ""
		"msg": "注册成功"
	}

2.教师注册

请求参数格式说明:

	{
		"username": "flyfish@ifeiyu.net",				    // 注册用户名
		"password": "flyfish",			       // 注册密码
		"grade": 1,							   //  注册年级(1: 小学 2: 初中 3: 高中)
		"identifier": 1,				          // 用户身份类别 (0: 学生 1: 教师)
		"nickname": "cls1991",               // 昵称
		"subject": 2,					          // 科目(1: 数学 2: 语文 3: 英语 4: 生物 5: 政治 6: 历史 7: 地理 8: 物理 9: 化学)
		"serial_number": "12345678",		   // 工作证号(暂定为8位数字)
		"options": "{\"phone_number\": \"15145102540\", ....}"    // 选填信息
	}

返回结果说明:

	{
		"code": 200,							// OK, 其余状态码均失败
		"data": "",
		"msg": "注册成功"
	}

###3 QueryUserQuestionList
请求问题列表

HTTP POST请求方式, 访问接口: http://123.59.71.144:10100/doQuestionAct/QueryUserQuestionList, 请求示例:

	curl -d "username=xxx&cur_page=xxx&page_size=xxx" "http://123.59.71.144:10100/doQuestionAct/QueryUserQuestionList"

请求参数格式说明:

	{
		"username": "flyfish@ifeiyu.net",                  // 用户名
		"cur_page": 1,                                     // 当前数据分页 (默认值: 1)
		"page_size": 15                                   // 每页显示数据条数 (默认值: 10)
	}

返回结果说明:

	{
		"code": 200,						      // OK
		"data": {
			"question_list":
				[
					{
						"question_id": 3,                               // 问题ID
						"question_username": "flyfish@ifeiyu.net",                // 提问者
						"avatar_url": "/data/avatars/flyfish.png",     // 头像索引
						"nickname": "cls1991",                        // 昵称
						"question_grade": 1,		                    // 问题对应的年级(1: 小学 2: 初中 3: 高中)
						"question_subject": 2,                        // 问题所属科目(1: 数学 2: 语文 3: 英语 4: 生物 5: 政治 6: 历史 7: 地理 8: 物理 9: 化学)
						"question_head" "xxx",                        // 系统随机注入的信息头部
						"quetion_content": "xxx",                     // 问题内容
						"question_pic_url": "xxx",                     // 问题相关的图片url
						"question_sound_url": "xxx",                  // 问题相关的录音url
						"question_score": 10,                         // 问题悬赏积分
						"answer_counts": 3,                           //  问题回答的数目
						"question_time": "2015-08-10 00:13:13"        // 提问时间
					},
					......
				],
			 "cur_page": 1,                  // 当前页数
			 "page_size": 15,                // 每页显示的数据条数
			 "counts": 30                    // 数据总条数
		},
		"msg": ""
	}

###4 PostQuestion
用户提问

HTTP POST请求方式, 访问接口: http://123.59.71.144:10100/doQuestionAct/PostQuestion, 请求示例:

	curl -d "username=xxx&grade=xxx&subject=xxx&content_type=xxx&question_content=xxx&question_score=xxx" "http://123.59.71.144:10100/doQuestionAct/PostQuestion"

请求参数格式说明:

	{
		"username": "flyfish@ifeiyu.net",			                // 用户名
		"grade": 1,							            // 年级(1: 小学 2: 初中 3: 高中)
		"subject": 2,                                // 科目(1: 数学 2: 语文 3: 英语 4: 生物 5: 政治 6: 历史 7: 地理 8: 物理 9: 化学)
		"question_content": "xxx",                   // 问题内容
		"question_score": 10			               // 问题悬赏积分
	}

返回结果说明:

	{
		"code": 200,						    // OK
		"data": "",
		"msg": "提问成功"
	}

###5 ConnectQuestion
收藏问题

HTTP POST请求方式, 访问接口: http://123.59.71.144:10100/doQuestionAct/ConnectQuestion, 请求示例:

	curl -d "username=xxx&question_id=xxx" "http://123.59.71.144:10100/doQuestionAct/ConnectQuestion"

请求参数格式说明:

	{
		"username": "flyfish@ifeiyu.net",                  // 用户名
		"question_id": 1001				          // 问题ID
	}

返回结果说明:

	{
		"code": 200,						   // Ok
		"data": "",
		"msg": "收藏成功"
	}

###6 SearchQuestion
用户搜索问题

HTTP POST请求方式, 访问接口: http://123.59.71.144:10100/doQuestionAct/SearchQuestion, 请求示例:

 	curl -d "username=xxx&question_content=xxx&cur_page=xxx&page_size=xxx&grade=xxx&subject=xxx" "http://123.59.71.144:10100/doQuestionAct/SearchQuestion"

 请求参数格式说明:

 	{
 		"username": "flyfish@ifeiyu.net",                      // 用户名
 		"question_content": "xxx",	                 // 查询的问题内容
 		"cur_page": 1,                              // 当前页数
 		"page_size": 20,                            // 每页显示的数据条数
 		"grade": 1,                                  // 年级 (可选值)
 		"subject": 1                                 // 科目 (可选值)
 	}

 返回结果说明:

	 {
	 	"code": 200,						      // OK
		"data": {
			"question_list":
				[
					{
							"question_id": 3,                               // 问题ID
							"question_username": "flyfish@ifeiyu.net",                // 提问者
							"avatar_url": "/data/avatars/flyfish.png",     // 头像索引
							"nickname": "cls1991",                          // 昵称
							"question_grade": 1,		                    // 问题对应的年级
							"question_subject": 2,                        // 问题所属科目(1: 数学 2: 语文 3: 英语 4: 生物 5: 政治 6: 历史 7: 地理 8: 物理 9: 化学)
							"question_head" "xxx",                        // 系统随机注入的信息头部
							"quetion_content": "xxx",                     // 问题内容
							"question_pic_url": "xxx",                     // 问题相关的图片url
							"question_sound_url": "xxx",                  // 问题相关的录音url
							"question_score": 10,                         // 问题悬赏积分
							"answer_counts": 3,                           //  问题回答的数目
							"question_time": "2015-08-10 00:13:13"        // 提问时间
						},
						......
				 ],
			 "cur_page": 1,                  // 当前页数
			 "page_size": 15,                // 每页显示的数据条数
			 "counts": 30                    // 数据总条数
		}
		 "msg": ""
	 }

###7 AnswerQuestion
回答问题

HTTP POST请求方式, 访问接口: http://123.59.71.144:10100/doQuestionAct/AnswerQuestion, 请求示例:

	curl -d "username=xxx&question_id=xxx&answer_content=xxx" "http://123.59.71.144:10100/doQuestionAct/AnswerQuestion"

请求参数格式说明:

	{
		"username": "flyfish@ifeiyu.net",                     // 用户名
		"question_id": 1001,		                // 回答的问题ID
		"answer_content": "xxx"                   // 回答的内容
	}

返回结果说明:

	{
		"code": 200,                             // OK
      	"data": "",
      	"msg": "回答成功"
	}

###8 AskQuestion
用户追问

HTTP POST请求方式, 访问接口: http://123.59.71.144:10100/doQuestionAct/AskQuestion, 请求示例:

	curl -d "username=xxx&ask_content=xxx&original_quetion_id=xxx&be_asked_username=xxx" "http://123.59.71.144:10100/doQuestionAct/AskQuestion"


请求参数格式说明:

	{
		"username": "flyfish@ifeiyu.net",                       // 追问者的用户名
		"ask_content": "xxx",                       // 追问内容
		"original_question_id": 1001,               // 原问题的ID
		"be_asked_username": "flyfish@ifeiyu.net"              // 被追问者的用户名
	}

返回结果说明:

	{
		"code": 200,			                       // OK
		"data": "",
		"msg": "追问成功"
	}

###9 QueryUserQuestionDetail
请求问题详细信息

HTTP POST请求方式, 访问接口: http://123.59.71.144:10100/doQuestionAct/QueryUserQuestionDetail, 请求示例:

	curl -d "username=xxx&question_id=xxx" "http://123.59.71.144:10100/doQuestionAct/QueryUserQuestionDetail"

请求参数格式说明:

	{
		"username": "flyfish@ifeiyu.net",                   // 用户名
		"question_id": 1001                      // 问题ID
	}

返回结果说明:

	{
		"code": 200,				           // OK
		"data": {
			"question_info": {
				"question_id": 3,                               // 问题ID
				"question_username": "flyfish@ifeiyu.net",                // 提问者
				"avatar_url": "/data/avatars/flyfish.png",     // 头像索引
				"nickname": "cls1991",                        // 昵称
				"question_grade": 1,		                    // 问题对应的年级(1: 小学 2: 初中 3: 高中)
				"question_subject": 2,                        // 问题所属科目(1: 数学 2: 语文 3: 英语 4: 生物 5: 政治 6: 历史 7: 地理 8: 物理 9: 化学)
				"question_head" "xxx",                        // 系统随机注入的信息头部
				"quetion_content": "xxx",                     // 问题内容
				"question_pic_url": "xxx",                     // 问题相关的图片url
				"question_sound_url": "xxx",                  // 问题相关的录音url
				"question_score": 10,                         // 问题悬赏积分
				"answer_counts": 3,                           //  问题回答的数目
				"question_status": 0,                         // 问题当前的状态 (0: 未解决 1: 已解决)
				"question_time": "2015-08-10 00:13:13"        // 提问时间
			},
			"answers_info": [[{
				"question_id": 3,                               // 问题ID
				"answer_id": 1,                                 // 回答ID
				"answer_username": "flyfish@ifeiyu.net",                // 回答者
				"avatar_url": "/data/avatars/flyfish.png",     // 头像索引
				"nickname": "cls1991",                       // 昵称
				"answer_content": "xxx",                     // 回答内容
				"answer_pic_url": "xxx",                     // 回答相关的图片url
				"answer_sound_url": "xxx",                   // 回答相关的录音url
				"is_accepted": 0,			                  // 是否被采纳
				"answer_time": "2015-08-10 00:13:13"        // 回答的最新时间
				},
				// 如果有追问
				{
					"ask_question_id": 1001,                // 追问产生的临时问题ID
					"ask_content": "xxx",                  // 追问内容
					"ask_pic_url": "xxx",                  // 追问相关的图片url
					"ask_sound_url": "xxx",               // 追问相关的录音url
					"ask_time": "xxx",                    // 追问时间
					"original_question_id": 3,            // 原问题的ID
					"be_asked_username": "flyfish13@ifeiyu.net",     // 被追问者的用户名
					"avatar_url": "/data/avatars/flyfish.png",     // 头像索引
					"nickname": "cls1991",                       // 昵称
					"ask_order": 1                       // 追问顺序
				},
				......
			],
			// 如果有其他用户回答
			.....
		  ]
		},
		"msg": ""
	}

###10 SignDaily
每日签到

HTTP POST请求, 访问接口: http://123.59.71.144:10100/doUserAct/SignDaily, 请求示例:

	curl -d "username=xxx" "http://123.59.71.144:10100/doUserAct/SignDaily"

请求参数格式说明:

	{
		"username": "flyfish@ifeiyu.net"	                     // 用户名
	}

返回结果说明:

	{
		"code": 200,		                 // OK
		"data": "",
		"msg": "签到成功"
	}

###11 QueryUserPointsDetail
请求用户积分明细

HTTP POST请求, 访问接口: http://123.59.71.144:10100/doUserAct/QueryUserPointsDetail, 请求示例:

	curl -d "username=xxx" "http://123.59.71.144:10100/doUserAct/QueryUserPointsDetail"

请求参数格式说明:

	{
		"username": "flyfish@ifeiyu.net"                 // 用户名
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
		},
		"msg": ""
	}

###12 FollowOther
关注其他用户

HTTP POST请求方式, 访问接口: http://123.59.71.144:10100/doUserAct/FollowOther, 请求示例:

	curl -d "username=xxx&other_name=xxx" "http://123.59.71.144:10100/doUserAct/FollowOther"

请求参数格式说明:

	{
		"username": "flyfish@ifeiyu.net",                  // 用户名
		"other_name": "flyfish13@ifeiyu.net"               // 其他用户
	}

返回结果说明:

	{
		"code": 200,                   // OK
		"data": "",
		"msg": "关注成功"
	}

###13 QueryFollowers
请求关注/粉丝列表

HTTP POST请求方式, 请求接口: http://123.59.71.144:10100/doUserAct/QueryFollowers, 请求示例:

	curl -d "username=xxx" "http://123.59.71.144:10100/doUserAct/QueryFollowers"

请求参数格式说明:

	{
		"username": "flyfish@ifeiyu.net"                 // 用户名
	}

返回结果说明:

	{
		"code": 200,                         // OK
		"data": {
				"follows_num": 10,            // 关注数
				"fans_num": 21   			   // 粉丝数
		},
		"msg": ""
	}

###14 QueryUserQuestionOrAnswerList
请求用户的提问/回答列表

HTTP POST请求方式, 访问接口: http://123.59.71.144:10100/doUserAct/QueryUserQuestionsOrAnswers, 请求示例:

	curl -d "username=xxx&identifier=xxx&is_part=xxx&cur_page=xxx&page_size=xxx" "http://123.59.71.144:10100/doUserAct/QueryUserQuestionsOrAnswers"

请求参数格式说明:

	{
		"username": "flyfish@ifeiyu.net",                // 用户名
        "identifier": 0,                               // 身份标志 (0: 学生 1: 教师)
        "is_part": 0,                                // 查询范围 (0: 全部 1: 部分[学生: 完成的问题 教师: 被采纳的回答])
        "cur_page": 1,                               // 当前分页
        "page_size": 20                             // 每页显示的条数
	}

返回结果说明:

	{
	 	"code": 200,						      // OK
		"data": {
			"question_list":
				[
					{
							"question_id": 3,                             // 问题ID
							"question_username": "flyfish@ifeiyu.net",                // 提问者
							"avatar_url": "/data/avatars/flyfish.png",     // 头像索引
							"nickname": "cls1991",                        // 昵称
							"question_grade": 1,		                    // 问题对应的年级
							"question_subject": 2,                        // 问题所属科目(1: 数学 2: 语文 3: 英语 4: 生物 5: 政治 6: 历史 7: 地理 8: 物理 9: 化学)
							"question_head" "xxx",                        // 系统随机注入的信息头部
							"quetion_content": "xxx",                     // 问题内容
							"question_pic_url": "xxx",                     // 问题相关的图片url
							"question_sound_url": "xxx",                  // 问题相关的录音url
							"question_score": 10,                         // 问题悬赏积分
							"answer_counts": 3,                           //  问题回答的数目
							"question_time": "2015-08-10 00:13:13"        // 提问时间
						},
						......
				 ],
			 "cur_page": 1,                  // 当前页数
			 "page_size": 15,                // 每页显示的数据条数
			 "counts": 30                    // 数据总条数
		}
		 "msg": ""
	 }

###15 QueryUserConnectionQuestionList
请求用户收藏问题列表

HTTP POST请求方式, 访问接口: http://123.59.71.144:10100/doQuestionAct/QueryUserConnectionQuestionList, 请求示例:

	curl -d "username=xxx" "http://123.59.71.144:10100/doQuestionAct/QueryUserConnectionQuestionList"

请求参数格式说明:

	{
		"username": "flyfish@ifeiyu.net"               // 用户名
	}

返回结果说明:

	{
	 	"code": 200,						      // OK
		"data": {
			"question_list":
				[
					{
							"question_id": 3,                             // 问题ID
							"question_username": "flyfish@ifeiyu.net",                // 提问者
							"avatar_url": "/data/avatars/flyfish.png",     // 头像索引
							"nickname": "cls1991",                        // 昵称
							"question_grade": 1,		                    // 问题对应的年级
							"question_subject": 2,                        // 问题所属科目(1: 数学 2: 语文 3: 英语 4: 生物 5: 政治 6: 历史 7: 地理 8: 物理 9: 化学)
							"question_head" "xxx",                        // 系统随机注入的信息头部
							"quetion_content": "xxx",                     // 问题内容
							"question_pic_url": "xxx",                     // 问题相关的图片url
							"question_sound_url": "xxx",                  // 问题相关的录音url
							"question_score": 10,                         // 问题悬赏积分
							"answer_counts": 3,                           //  问题回答的数目
							"question_time": "2015-08-10 00:13:13"        // 提问时间
						},
						......
				 ],
			 "cur_page": 1,                  // 当前页数
			 "page_size": 15,                // 每页显示的数据条数
			 "counts": 30                    // 数据总条数
		}
		 "msg": ""
	 }

###16 ValidEmail
验证邮箱是否可用

HTTP POST请求方式, 访问接口: http://123.59.71.144:10100/doEmailAct/ValidEmail, 请求示例:

	curl -d "email_address=xxx" "http://123.59.71.144:10100/doEmailAct/ValidEmail"

请求参数格式说明:

    {
		"email_address": "flyfish@ifeiyu.net"
    }

返回结果说明:

	{
    	"code": 200,						// OK
        "data": "",
        "msg": ""
    }

###17 ChangePassword
修改密码

HTTP POST请求方式, 访问接口: http://123.59.71.144:10100/doUserAct/ChangePassword, 请求示例:

	curl -d "username=xxx&old_password=xxx&new_password=xxx" "http://123.59.71.144:10100/doUserAct/ChangePassword"

请求参数格式说明:

	{
		"username": "flyfish@ifeiyu.net",                         // 用户名
		"old_password": "flyfish",                                // 旧密码
		"new_password": "flyfish12",                              // 新密码
	}

返回结果说明:

	{
		"code": 200,                            // OK
		"data": "",
		"msg": "修改密码成功"
	}

###18 AboutUs
关于我们

HTTP POST请求方式, 访问接口: http://123.59.71.144:10100/doUserAct/AboutUs, 请求示例:

	curl -d "username=xxx" "http://123.59.71.144:10100/doUserAct/AboutUs"

请求参数格式说明:

	{
		"username": "flyfish@ifeiyu.net"                         // 用户名
	}

返回结果说明:

	{
		"code": 200,                              // OK
		"data": {
			"content": "哈尔滨市共有教师10万人，中小学学生100万人，目前缺乏有效的沟通桥梁。哈尔滨教育互动平台致力于打造人人乐用的学习服务平台，通过高效、智能、精准地匹配师生资源，为老师及学生提供多种增值服务和学习工具，创建一个专业、简单、智能、安全的高品质学习服务的第三方平台，让学习变得更加容易、平等和高效，让所有有知识、技能、才华的人都能够在这个平台上成为老师，让所有需要知识、技能、才华的人都能够在这个平台上找到他们学习的榜样。在让跟谁学成为一种生活方式的同时，跟谁学也在全力打造更富活力、更加健康的教育生态圈。"
		},
		"msg": ""
	}

###19 FeedBack
意见反馈

HTTP POST请求方式, 访问接口: http://123.59.71.144:10100/doUserAct/FeedBack, 请求示例:

	curl -d "username=xxx&content=xxx" "http://123.59.71.144:10100/doUserAct/FeedBack"

请求参数格式说明:

	{
		"username": "flyfish@ifeiyu.net",                             // 用户名
		"content": "flyfish, zzz"                                    // 反馈内容
	}

返回结果说明:

	{
		"code": 200,                       // OK
		"data": "",
		"msg": "提交反馈成功"
	}

###20 ModifyPersonalInformation
修改个人信息

HTTP POST请求方式, 访问接口: http://123.59.71.144:10100/doUserAct/ModifyPersonalInformation, 请求示例:

	curl -d "username=xxx&props={\"nickname\": xxx, ...}" "http://123.59.71.144:10100/doUserAct/ModifyPersonalInformation"

请求参数格式说明:

	{
		"username": "flyfish@ifeiyu.net",                      // 用户名
		"props": "{\"nickname\": \"zzz\", ....}"               // 更新的数据域
	}

返回结果说明:

	{
		"code": 200,
		"data": "",
		"msg": "修改成功"
	}

###21 AdoptAnswer
采纳回答

HTTP POST请求方式, 访问接口: http://123.59.71.144:10100/doQuestionAct/AdoptAnswer", 请求示例:

	curl -d "username=xxx&question_id=xxx&answer_id=xxx&answer_username=xxx" "http://123.59.71.144:10100/doQuestionAct/AdoptAnswer"

请求参数格式说明:

	{
    	"username": "flyfish@ifeiyu.net",                  // 用户名
        "question_id": 2,                                  // 原问题ID
        "answer_id": 1001,                                // 回答的ID
        "answer_username": "flyfish13@ifeiyu.net"        // 回答者的用户名
    }

返回结果说明:

	{
    	"code": 200,                   // OK
        "data": "",
        "msg": "采纳成功"
    }

###22 QueryAllInformation
请求用户所有信息 (供客户端进入"我的"页面使用)

HTTP POST请求方式, 访问接口: http://123.59.71.144:10100/doQuestionAct/QueryAllInformation, 请求示例:

	curl -d "username=xxx&identifier=xxx" "http://123.59.71.144:10100/doQuestionAct/QueryAllInformation"

请求参数格式说明:

	{
    	"username": "flyfish@ifeiyu.net",                   // 用户名
        "identifier": 0                                     // 身份标志 (0: 学生 1: 教师)
    }

返回结果说明:

	{
    	"code": 200,                               // OK
        "data": {
    		"user_info": {
      			"level_desc": "学渣",             // 称号
      			"total_points": 175,             // 总学分
      			"user_level": 1                 // 等级
    		},
    		"relation_info": {
      			"follows_num": 1,                // 关注数
      			"fans_num": 0                    // 粉丝数
    		},
            // 学生
    		"question_info": {
      			"solved_questions": 0,           // 已完成的问题数
      			"total_questions": 46           // 问题总数
    		}
            // 教师
            "answer_info": {
            	"total_answers": 30,           // 总回答数
                "accepted_answers": 10         // 被采纳的回答数
            }
  		}
    }
