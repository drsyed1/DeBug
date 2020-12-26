import os
import time
import datetime

import pyrogram
    
    
user_session_string = os.environ.get("1BVtsOHwBuwqrsinlWxs5au0hdAmI3kcYtpy5BK97xaZda6EDkiEIA90r0bnjM6A6yVjxfBRKDfzkifyOSIccS5MqoiCNPD_3cb1b8Ox4htuyKpOtSZpbtxyO6iM2k73uUMEBzd4f1eu9mqufc1nH2MkMjo_F4XAGTnyNwZ1U876CX9yYTr0sM0bRMCQ9nz8U_00wJwbINrCtTJwhckVqiVEzy7FjmKF2swH5wJw89VgXDGjZ53kC6j2GceYeuMhdXr1xsM557XWjznTWsvVUoKG4MF2jM0XYwOwnfJmqLi5Z3uUUggXnT2OGjvi9wjB-P-dYne5JbYMcxmRP28mq9oP4DDOYmso=")
bots = os.environ.get('@WhiteEyeRenameBot'), ('@WhiteEyeUrlUploaderBot'), ('@WhiteEyeYouTubeBot'), ('@WhiteEyeDeleteAllBot'), ('@WhiteEyeCompressorBot'), ('@Miss_ArantxaBot'), ('@WhiteEyeSubtitleBot'), ('@WhiteEyeLinkToFileBot'), ('@WhiteEyeGDriveBot'), ('@WhiteEyeTelegraphBot'), ('@WhiteEyeForceSubscriberBot'), ('@WhiteEyeUltraTonBot'), ('@WhiteEyeTagRemoverBot')
bot_owner = os.environ.get("@Mr_StarLords")
update_channel = os.environ.get("-1001484903966")
api_id = (os.environ.get("1715074"))
api_hash = os.environ.get("0c8fb6a43409019900aa98f439eceec4")

user_client = pyrogram.client(
    user_session_string, api_id=api_id, api_hash=api_hash)


def main():
        while True:
            print("[INFO] starting to check uptime..")
            edit_text = f"@{update_channel} Bot's Uptime Status.(Updated every 15 mins)\n\n"
            for bot in bots:
                print(f"[INFO] checking @{bot}")
                snt = user_client.send_message(bot, '/start')

                time.sleep(15)

                msg = user_client.get_history(bot, 1)[0]
                if snt.message_id == msg.message_id:
                    print(f"[WARNING] @{bot} is down")
                    edit_text += f"@{bot} status: `Down`\n\n"
                    user_client.send_message(bot_owner,
                                             f"@{bot} status: `Down`")
                else:
                    print(f"[INFO] all good with @{bot}")
                    edit_text += f"@{bot} status: `Up`\n\n"
                user_client.read_history(bot)

            utc_now = datetime.datetime.utcnow()
            ist_now = utc_now + datetime.timedelta(minutes=30, hours=5)

            edit_text += f"__last checked on \n{str(utc_now)} UTC\n{ist_now} IST__"

            user_client.edit_message_text(update_channel, status_message_id,
                                         edit_text)
            print(f"[INFO] everything done! sleeping for 15 mins...")

            time.sleep(15 * 60)


main()    
