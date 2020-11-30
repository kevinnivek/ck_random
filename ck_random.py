#!/usr/bin/python
import time,datetime,random,textwrap
import Adafruit_CharLCD as LCD


# Raspberry Pi pin configuration:
lcd_rs        = 25  # Note this might need to be changed to 21 for older revision Pi's.
lcd_en        = 24
lcd_d4        = 23
lcd_d5        = 17
lcd_d6        = 18
lcd_d7        = 22
lcd_backlight = 2

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           lcd_columns, lcd_rows, lcd_backlight)

current_date = datetime.datetime.now()

s_nouns = ["A hobo", "Dondald Trump", "Bradley cooper", "Some guy", "A man with slimes", "A hobo with cheese", "A hobo with slimes", "Benjamin Moore", "Bradley", "A penis", "A sex dwarf", "A sexual man", "A sexual woman", "A sexual person", "A stinky man", "Mr Dressup", "Casey Jones", "Suzanne", "Suzy", "Susan", "Sue", "Kevin", "Kevvy", "Duncan", "Dunky", "Duncaroo", "Mike", "Hawcko", "Mike Hawcko", "Kathryn", "Lenny", "Leonardo", "Rebekah", "Danny", "Adele", "Cher", "Lela", "Dennis", "Paolo", "Anul", "A beggar"]
p_nouns = ["A series of sexual hobos", "Sexualized cats", "Sexualized dogs", "Sexualized skunks", "Sexy raccoons", "Men with soft penises", "Sexy grandmas", "Hot grandpas", "Sex robots", "Jo Bro's", "Dungeon Masters", "Erect Dwarves", "Multiple Kevins", "Two Suzys", "Cluster of Duncans"]
s_verbs = ["licks", "sucks", "fucks", "breathes", "looks at", "meets with", "punches", "kicks", "bites", "screams", "decapitates", "sits on", "injects fluids", "gets juices on", "lubes", "moans on", "rubs", "fingers", "fists", "pinches", "tickles", "sniffs", "smells", "gawks", "coats", "slathers", "pokes", "presses", "inches", "cuts", "wipes", "cleans", "clenses", "purifies", "wet wipes", "lubricates", "mounts"]
p_verbs = ["lick", "suck", "fuck", "breathe", "meet with", "look at", "punch", "kick", "bite", "scream", "decapitate", "lube", "moan", "rub", "penetrate", "finger", "sniff", "smell", "tickle", "grasp"]
infinitives = ["to make sex.", "for no reason at all.", "because anal glue is important.", "to be able to explode with ecstac.", "to know more about sex swings.", "until their testicles were swollen.", "all day and all night.", "until there was nothing left.", "until their voice were hoarse from screaming.", "unil their soft moans ceased.", "for whatever reson.", "until their balls hurt.", "until the urethra exploded.", "to make fuck.", "to sexually rub.", "completely randomly.", "until the fluids ran dry."]

def sing_sen_maker():
    return str(random.choice(s_nouns)) + ' ' + str(random.choice(s_verbs)) + ' ' + str(random.choice(s_nouns).lower()) or str(random.choice(p_nouns).lower()) + ' ' + str(random.choice(infinitives))

while True:
    message = sing_sen_maker()
    if len(message) <= 32:
        break

message = textwrap.fill(message,width=16)
#print message
lcd.clear()
lcd.message(textwrap.fill(message, 16))
for i in range(lcd_columns-len(message)):
    time.sleep(0.5)
    lcd.move_right()
for i in range(lcd_columns-len(message)):
    time.sleep(0.5)
    lcd.move_left()
