import discord
import random

client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!hello':
        response = "Hi, I am Apollo! Type !screen to proceed with the screening."
        await message.channel.send(response)

    # Level 1:
    elif message.content == '!screen':
        response = "**Let the screening begin... \nDo any of the following apply to you? **\n\n*a. I am fully vaccinated " \
                   "against " \
                   "COVID-19 (it has been 14 days or more since your final dose of either a two-dose or a one-dose " \
                   "vaccine series)*\n\n *b. I have tested positive for COVID-19 in the last 90 days (and since been " \
                   "cleared)*\n\n** To reply yes, type y, and to reply no, type n **"
        await message.channel.send(response)

        def check(msg):
            return msg.author == message.author and msg.channel == message.channel and msg.content.lower() in ["y", "n"]

        msg = await client.wait_for("message", check=check)
        # Level 2, YY
        if msg.content.lower() == "y":
            await message.channel.send("**In the last 14 days, have you travelled outside of Canada and been told to "
                                       "quarantine (per the federal quarantine requirements)?**")

            msg = await client.wait_for("message", check=check)

            if msg.content.lower() == "y":
                await message.channel.send("**DO NOT ATTEND THIS EVENT**")
            # Level 2, YN
            else:
                await message.channel.send("**Has a doctor, health care provider, or public health unit told you that "
                                           "you should currently be isolating (staying at home)?**\nThis can be "
                                           "because of an outbreak or contact tracing.")

                msg = await client.wait_for("message", check=check)
                # Level 3, YNY
                if msg.content.lower() == "y":
                    await message.channel.send( "**DO NOT ATTEND THIS EVENT**")

                else:
                    await message.channel.send(
                        "**Are you currently experiencing any of these symptoms?**\nChoose any/all that are new, "
                        "worsening, and not related to other known causes or conditions you already have.\n\n**Fever "
                        "and/or chills**\nTemperature of 37.8 degrees Celsius/100 degrees Fahrenheit or "
                        "higher\n\n**Cough or barking cough**\nContinuous, more than usual, making a "
                        "whistling noise when breathing (not related to asthma, post-infectious "
                        "reactive airways, or other known causes or conditions you already "
                        "have)\n\n**Shortness of breath**\nOut of breath, unable to breathe deeply "
                        "(not related to asthma or other known causes or conditions you already "
                        "have)\n\n**Decrease or loss of taste or smell**\nNot related to seasonal "
                        "allergies, neurological disorders, or other known causes or conditions "
                        "you already have\n\n**Nausea, vomiting, and/or diarrhea**\nNot related to "
                        "irritable bowel syndrome, anxiety, menstrual cramps, or other known "
                        "causes or conditions you already have")

                    msg = await client.wait_for("message", check=check)

                    if msg.content.lower() == "y":
                        await message.channel.send("**DO NOT ATTEND THIS EVENT**") # might recommend a hospital

                    else:
                        await message.channel.send("**In the last 10 days, have you tested positive on a rapid antigen "
                                                   "test or home-based self-testing kit?**\nIf you have since tested negative on a lab-based PCR test, select No.")

                        msg = await client.wait_for("message", check=check)

                        if msg.content.lower() == "y":
                            await message.channel.send("**DO NOT ATTEND THIS EVENT**")

                        else:
                            await message.channel.send("**YOU CAN ATTEND THIS EVENT**")

        # Level 2, N, YASER START HERE
        else:
            await message.channel.send('**In the last 14 days, have you travelled outside of Canada?**\n'
                                        'If travel was only for a cross-border custody arrangement, select “No.”')

            msg = await client.wait_for("message", check=check)

            if msg.content.lower() == "y":
                await message.channel.send("**DO NOT ATTEND THIS EVENT**")
                return

            # Level 3, NN
            else:
                await message.channel.send(
                    "**Has a doctor, health care provider, or public health unit told you that you should currently be isolating (staying at home)?**\n"
                    "This can be because of an outbreak or contact tracing.")

                msg = await client.wait_for("message", check=check)

                if msg.content.lower() == "y":
                    await message.channel.send("**DO NOT ATTEND THIS EVENT**")
                    return

                # Level 4, NNN
                else:
                    await message.channel.send(
                        "**In the last 10 days, have you been identified as a “close contact” of someone who currently has COVID-19?**"
                        '\nIf public health has advised you that you do not need to self-isolate, select “No.”')

                    msg = await client.wait_for("message", check=check)

                    if msg.content.lower() == "y":
                        await message.channel.send("**DO NOT ATTEND THIS EVENT**")
                        return
                    
                    # Level 5, NNNN
                    else:
                        await message.channel.send(
                            "**In the last 10 days, have you received a COVID Alert exposure notification on your cell phone?**"
                            '\nIf you already went for a test and got a negative result, select “No.”')

                        msg = await client.wait_for("message", check=check)

                        if msg.content.lower() == "y":
                            await message.channel.send("**DO NOT ATTEND THIS EVENT**")
                            return

                        # Level 6, NNNNN
                        else:
                            await message.channel.send(
                                "**Are you currently experiencing any of these symptoms?**\n\n**Fever and/or "
                                "chills**\nTemperature of 37.8 degrees Celsius/100 degrees Fahrenheit or "
                                "higher\n\n**Cough or barking cough**\nContinuous, more than usual, making a "
                                "whistling noise when breathing (not related to asthma, post-infectious "
                                "reactive airways, or other known causes or conditions you already "
                                "have)\n\n**Shortness of breath**\nOut of breath, unable to breathe deeply "
                                "(not related to asthma or other known causes or conditions you already "
                                "have)\n\n**Decrease or loss of taste or smell**\nNot related to seasonal "
                                "allergies, neurological disorders, or other known causes or conditions "
                                "you already have\n\n**Nausea, vomiting, and/or diarrhea**\nNot related to "
                                "irritable bowel syndrome, anxiety, menstrual cramps, or other known "
                                "causes or conditions you already have")
                            
                            msg = await client.wait_for("message", check=check)

                            if msg.content.lower() == "y":
                                await message.channel.send("**DO NOT ATTEND THIS EVENT**")
                                return

                            # Level 7, NNNNNN
                            else:
                                await message.channel.send(
                                    "**Is anyone you live with currently experiencing any new COVID-19 symptoms and/or waiting for test results after experiencing symptoms?**"
                                    '\nIf the person got a COVID-19 vaccine in the last 48 hours and is experiencing a mild headache, fatigue, muscle aches, and/or joint pain that only began after vaccination, select “No.”')

                                msg = await client.wait_for("message", check=check)

                                if msg.content.lower() == "y":
                                    await message.channel.send("**DO NOT ATTEND THIS EVENT**")
                                    return
                                
                                # Level 8, NNNNNNN
                                else:
                                    await message.channel.send(
                                        "**In the last 10 days, have you tested positive on a rapid antigen test or home-based self-testing kit?**"
                                        '\nIf you have since tested negative on a lab-based PCR test, select "No."')
                                    
                                    msg = await client.wait_for("message", check=check)

                                    if msg.content.lower() == "y":
                                        await message.channel.send("**DO NOT ATTEND THIS EVENT**")
                                        return
                                    
                                    else:
                                        await message.channel.send("**YOU CAN ATTEND THIS EVENT**")
                                        return
                    

                
    


client.run("ODg4Nzg3MjE4NzAzOTk5MDE2.YUXxmQ.qR-61OtwZuJj2DWEqM3oKGU4Vxk")

print("I'm Online")
