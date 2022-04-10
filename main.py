import discord
from discord_components import DiscordComponents, Button, ButtonStyle, Interaction
import asyncio

client = discord.Client()

DiscordComponents(client)

token = "토큰" #봇토큰

common_id = '123456789012345678' #기본문의 카테고리 id

common = '일반문의：'

charge_id = '123456789012345678' #충전문의 카테고리 id

charge = '충전문의：'

p_id = '123456789012345678' #구매문의 카테고리 id
 
purchase = '구매문의：'

q_id = '123456789012345678' #질문 카테고리 id

qs = '질문：'

member_mention = '||<@123456789012345678>, <@123456789012345678> ||' #이런식으로 관리자 아이디 적으세요 (티켓열리면멘션)

admin = [123456789012345678, 123456789012345678] #관리자 아이디 적으세요

def embed(description):
    embed = discord.Embed(title="제목", description=description, color=0x2f3136) #title에는 티켓임베드 제목에 뜰 이름 (그외 별다른거 수정 x)
    return embed

@client.event
async def on_ready():
    print(" ")
    print("봇 작동중")
    print(" ")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("티켓관리"))

@client.event
async def on_message(message):
    if message.author.bot: #봇이면 반응x
        return
    if message.author.id in admin:
        if message.content == "!티켓": #!티켓 명령어
            await message.delete() #메시지 자동으로 삭제
            if message.author.guild_permissions.administrator: #관리자라면 작동하기
                await message.channel.send(embed=embed("```diff\n+ 티켓문의를 하시려면 아래버튼을 눌러주세요```"), components=[[Button(label="💌 기본문의", id="ticket", style=ButtonStyle.blue), Button(label="🧾 충전문의", id="charge", style=ButtonStyle.green), Button(label="🛒 구매&예약문의", id="p", style=ButtonStyle.red) ,Button(label="💬 질문", id="q", style=ButtonStyle.gray)]])
            else: #관리자가 아니라면 밑 메시지 보내기
                await message.channel.reply("관리자만 사용가능한 명령어입니다.")
    if message.content.startswith("!닫기"): #!닫기 명령어
        if message.author.guild_permissions.administrator:
            await message.channel.send("명령어로 닫기를 하셨습니다", components=[[Button(label="💥티켓닫기", custom_id="close", style=ButtonStyle.red)]])
        else: #관리자가 아니라면 밑 메시지 보내기
            await message.channel.reply("관리자만 사용가능한 명령어입니다.")

    if message.channel.id == 874316896709787668: #구매후기칸에 자동으로 이모지달기 (채널 아이디 수정)
        await message.add_reaction('<:cat:944548683360382996>') #달 이모지

@client.event
async def on_button_click(interaction: Interaction):

    if interaction.component.custom_id == "ticket": #기본문의 버튼이 눌렸다면

        i = 0
        for channel in interaction.guild.channels:
            if str(channel.name) == f'{common}' + (str(interaction.user).lower()).replace("#", ""):
                print(channel.name)
                i = 1
                break

        if i == 0:
            overwrites = {
                interaction.guild.default_role: discord.PermissionOverwrite(read_messages=False, send_messages=False),
                interaction.user: discord.PermissionOverwrite(read_messages=True, send_messages=True),
            }
            channel = await interaction.guild.create_text_channel(f'{common}' + str(interaction.user).lower(), overwrites=overwrites, category=interaction.guild.get_channel(int(common_id)))
            await interaction.respond(embed=embed(f" :ok_hand:  <#{str(channel.id)}>로 이동해주세요."), components = [
                [
                Button(label = "💌 TICKET", style=ButtonStyle.URL, url=f"https://discord.com/channels/{interaction.guild.id}/{channel.id}")]
            ])
            await channel.send(embed=embed(f"<@{str(interaction.user.id)}>\n\n[팀뷰어다운로드](https://www.teamviewer.com/ko/teamviewer-automatic-download/)\n\n[애니데스크다운로드](https://anydesk.com/en)\n\n```cs\n# 원격문의일시 팀뷰어 혹은 애니데스크 설치후 아이디 적어주세요\n# 팀뷰어일시 비번도 적어주세요\n' 충전문의일시 입금내역스샷 보내주세요 '\n```\n```관리자를 부르는중입니다...```"), components=[[Button(label="💥티켓닫기", custom_id="close", style=ButtonStyle.red)]])
            await channel.send(f"<@{interaction.user.id}> {member_mention}")
            for i in range(0,int(len(admin))):
                user = await client.fetch_user(admin[i])
                await user.send(f'문의알림 : <@{str(interaction.user.id)}> 님이 일반 문의티켓을 열었습니다', components = [
                [
                Button(label = "💌 TICKET", style=ButtonStyle.URL, url=f"https://discord.com/channels/{interaction.guild.id}/{channel.id}")]
            ])
        else:
            await interaction.respond(embed=embed(f"❌ <#{str(channel.id)}>이미 티켓채널이 존재합니다."))

    if interaction.component.custom_id == "charge":

        i = 0
        for channel in interaction.guild.channels:
            if str(channel.name) == f'{charge}' + (str(interaction.user).lower()).replace("#", ""):
                print(channel.name)
                i = 1
                break

        if i == 0:
            overwrites = {
                interaction.guild.default_role: discord.PermissionOverwrite(read_messages=False, send_messages=False),
                interaction.user: discord.PermissionOverwrite(read_messages=True, send_messages=True),
            }
            channel = await interaction.guild.create_text_channel(f'{charge}' + str(interaction.user).lower(), overwrites=overwrites, category=interaction.guild.get_channel(int(charge_id)))
            await interaction.respond(embed=embed(f" :ok_hand:  <#{str(channel.id)}>로 이동해주세요."), components = [
                [
                Button(label = "💌 TICKET", style=ButtonStyle.URL, url=f"https://discord.com/channels/{interaction.guild.id}/{channel.id}")]
            ])
            await channel.send(embed=embed(f"<@{str(interaction.user.id)}>\n\n```cs\n# 계좌충전문의 일시 입금내역을 스샷하여 전송해주십시오\n' 5분정도는 자충을 기다려주십시오 '\n# 관리자가 확인후 수동충전해드립니다 \n```\n```관리자를 부르는중입니다...```"), components=[[Button(label="💥티켓닫기", custom_id="close", style=ButtonStyle.red)]])
            await channel.send(f"<@{interaction.user.id}>  {member_mention}")
            owner = [admin]
            for i in range(0,int(len(admin))):
                user = await client.fetch_user(admin[i])
                await user.send(f'문의알림 : <@{str(interaction.user.id)}> 님이 충전 문의티켓을 열었습니다', components = [
                [
                Button(label = "💌 TICKET", style=ButtonStyle.URL, url=f"https://discord.com/channels/{interaction.guild.id}/{channel.id}")]
            ])

        else:
            await interaction.respond(embed=embed(f"❌ <#{str(channel.id)}>이미 티켓 채널이 존재합니다."))

    if interaction.component.custom_id == "q":

        i = 0
        for channel in interaction.guild.channels:
            if str(channel.name) == f'{qs}' + (str(interaction.user).lower()).replace("#", ""):
                print(channel.name)
                i = 1
                break

        if i == 0:
            overwrites = {
                interaction.guild.default_role: discord.PermissionOverwrite(read_messages=False, send_messages=False),
                interaction.user: discord.PermissionOverwrite(read_messages=True, send_messages=True),
            }
            channel = await interaction.guild.create_text_channel(f'{qs}' + str(interaction.user).lower(), overwrites=overwrites, category=interaction.guild.get_channel(int(q_id)))
            await interaction.respond(embed=embed(f" :ok_hand:  <#{str(channel.id)}>로 이동해주세요."), components = [
                [
                Button(label = "💌 TICKET", style=ButtonStyle.URL, url=f"https://discord.com/channels/{interaction.guild.id}/{channel.id}")]
            ])
            await channel.send(embed=embed(f"<@{str(interaction.user.id)}>\n\n```bash\n# 밑 카테고리를 보고오셧나요?``` <#935539209224220683> ```cs\n# 그 외 질문일시 내용을 적어주세요\n```\n```관리자를 부르는중입니다...```"), components=[[Button(label="💥티켓닫기", custom_id="close", style=ButtonStyle.red)]])
            await channel.send(f"<@{interaction.user.id}>  {member_mention}")
            owner = [admin]
            for i in range(0,int(len(admin))):
                user = await client.fetch_user(admin[i])
                await user.send(f'문의알림 : <@{str(interaction.user.id)}> 님이 질문 티켓을 열었습니다', components = [
                [
                Button(label = "💌 TICKET", style=ButtonStyle.URL, url=f"https://discord.com/channels/{interaction.guild.id}/{channel.id}")]
            ])

        else:
            await interaction.respond(embed=embed(f"❌ <#{str(channel.id)}>이미 티켓 채널이 존재합니다."))

    if interaction.component.custom_id == "p":
        i = 0
        for channel in interaction.guild.channels:
            if str(channel.name) == f'{purchase}' + (str(interaction.user).lower()).replace("#", ""):
                print(channel.name)
                i = 1
                break

        if i == 0:
            overwrites = {
                interaction.guild.default_role: discord.PermissionOverwrite(read_messages=False, send_messages=False),
                interaction.user: discord.PermissionOverwrite(read_messages=True, send_messages=True),
            }
            channel = await interaction.guild.create_text_channel(f'{purchase}' + str(interaction.user).lower(), overwrites=overwrites, category=interaction.guild.get_channel(int(p_id)))
            await interaction.respond(embed=embed(f" :ok_hand:  <#{str(channel.id)}>로 이동해주세요."), components = [
                [
                Button(label = "💌 TICKET", style=ButtonStyle.URL, url=f"https://discord.com/channels/{interaction.guild.id}/{channel.id}")]
            ])
            await channel.send(embed=embed(f"<@{str(interaction.user.id)}>\n\n```cs\n# 예약문의 일시 원하는제품 수량 말씀해주세요\n# 구매문의 일시 구매하실제품을 말해주세요\n' 티켓을 열고 10분이내에 채팅이없을시 티켓이 닫힙니다 '\n```\n```관리자를 부르는중입니다...```"), components=[[Button(label="💥티켓닫기", custom_id="close", style=ButtonStyle.red)]])
            await channel.send(f"<@{interaction.user.id}>  {member_mention}")
            owner = [admin]
            for i in range(0,int(len(admin))):
                user = await client.fetch_user(admin[i])
                await user.send(f'문의알림 : <@{str(interaction.user.id)}> 님이 구매 문의티켓을 열었습니다', components = [
                [
                Button(label = "💌 TICKET", style=ButtonStyle.URL, url=f"https://discord.com/channels/{interaction.guild.id}/{channel.id}")]
            ])

        else:
            await interaction.respond(embed=embed(f"❌ <#{str(channel.id)}>이미 티켓 채널이 존재합니다."))

    if interaction.component.custom_id == "close":
        await interaction.respond(content="> 닫을건지 선택해주세요")
        a1 = discord.Embed(title="제목",
                           description=f"```티켓닫기를 취소하려면 닫기취소버튼을. \n진행하려면 티켓닫기버튼을눌러주세요```  <@{interaction.user.id}>님이 티켓닫기를 요청하셨습니다 ",
                           color=0x2f3136)
        await interaction.channel.send(embed=a1, components=[[Button(label="💥닫기취소", custom_id="cancle", style=ButtonStyle.gray),
                                                              Button(label="💥티켓닫기", custom_id="close1", style=ButtonStyle.red)]])
    if interaction.component.custom_id == "cancle":
        await interaction.message.delete()
        a3 = discord.Embed(title="제목",
                           description=f"```diff\n- 티켓닫기가 취소되었습니다```  <@{interaction.user.id}>님이 티켓 닫기를 취소하셨습니다. ",
                           color=0x2f3136)
        cancle_message = await interaction.channel.send(embed=a3)
        await asyncio.sleep(3)
        await cancle_message.delete()
    if interaction.component.custom_id == "close1":
        await interaction.respond(content="> 티켓이 10초후 닫힙니다")
        a2 = discord.Embed(title="제목",
                           description=f"```💥 10초후에 티켓이 삭제됩니다.```  <@{interaction.user.id}>님이 티켓을 닫았습니다. ",
                           color=0x2f3136)
        await interaction.channel.send(embed=a2)
        await asyncio.sleep(10)
        await interaction.channel.delete()
        return

client.run(token)
