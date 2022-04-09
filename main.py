import pygame, sys

screen_width = 1200
screen_height = 700

Bpos = (325, 400)
BTpos = (250, 55)
Cpos = (1000, 360)
Currpos = (1000,40)
Plowpos = (1000,140)
Rewpos = (1000, 470)
Owpos = (1000, 240)

TCpos = (1350,640)
TCurrpos = (1350,310)
TPlowpos = (1350,420)
TRewpos = (1350,750)
TOwpos =  (1350,530)

TdCpos = (750, 360)
TdCurrpos = (750,40)
TdPlowpos = (750,140)
TdRewpos = (750, 470)
TdOwpos = (750, 240)

CurrsorPrice = 100
Plow_price = 200
Owen_Price = 300
CheffPrice = 400
ReviewPrice = 500

Owens = 0
Rewievs = 0
Plows = 0
currsor = 0
cheffs = 0
clicks = 0
Hold = False

additional_Click = 1

screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
pygame.init()

main_Font = pygame.font.Font('fonts/Font.ttf', 50)
Click_message = main_Font.render(f'{clicks}', False, "black")
Click_message = pygame.transform.scale2x((Click_message))
Clicks_rect = Click_message.get_rect(center = BTpos)

TCC_message = main_Font.render(f'{clicks}', False, "black")
TCC_message = pygame.transform.scale2x((TCC_message))
TCC_rect = Click_message.get_rect(center = TdCpos)

TCCU_message = main_Font.render(f'{clicks}', False, "black")
TCCU_message = pygame.transform.scale2x((TCCU_message))
TCCU_rect = Click_message.get_rect(center = TdCurrpos)

TCP_message = main_Font.render(f'{clicks}', False, "black")
TCP_message = pygame.transform.scale2x((TCP_message))
TCP_rect = Click_message.get_rect(center = TdPlowpos)

TCR_message = main_Font.render(f'{clicks}', False, "black")
TCR_message = pygame.transform.scale2x((TCR_message))
TCR_rect = Click_message.get_rect(center = TdRewpos)

TCO_message = main_Font.render(f'{clicks}', False, "black")
TCO_message = pygame.transform.scale2x((TCO_message))
TCO_rect = Click_message.get_rect(center = TdOwpos)

butt_surf  = pygame.image.load(("art/Button.png"))
butt_surf = pygame.transform.scale2x(butt_surf)
butt_rect = butt_surf.get_rect(center = Bpos)

cheff_surf  = pygame.image.load(("art/cheff.png"))
cheff_surf = pygame.transform.scale2x(cheff_surf)
cheff_rect = cheff_surf.get_rect(center = Cpos)
cheffs_message = main_Font.render(f'{cheffs}', False, "black")
cheffs_message = pygame.transform.scale2x((cheffs_message))
Tcheff_rect = butt_surf.get_rect(center=TCpos)

curr_surf  = pygame.image.load(("art/currsos.png"))
curr_surf = pygame.transform.scale2x(curr_surf)
curr_rect = curr_surf.get_rect(center = Currpos)
currsor_message = main_Font.render(f'{currsor}', False, "black")
currsor_message = pygame.transform.scale2x((currsor_message))
Tcurr_rect = butt_surf.get_rect(center=TCurrpos)

plow_surf  = pygame.image.load(("art/plow.png"))
plow_surf = pygame.transform.scale2x(plow_surf)
plow_rect = plow_surf.get_rect(center = Plowpos)
plow_message = main_Font.render(f'{Plows}', False, "black")
plow_message = pygame.transform.scale2x((plow_message))
Tpow_rect = butt_surf.get_rect(center=TPlowpos)

rew_surf  = pygame.image.load(("art/review.png"))
rew_surf = pygame.transform.scale2x(rew_surf)
rew_rect = rew_surf.get_rect(center = Rewpos)
Rew_message = main_Font.render(f'{Rewievs}', False, "black")
Rew_message = pygame.transform.scale2x((Rew_message))
Trew_rect = butt_surf.get_rect(center=TRewpos)

Ow_surf  = pygame.image.load(("art/owen.png"))
Ow_surf = pygame.transform.scale2x(Ow_surf)
Ow_rect = Ow_surf.get_rect(center = Owpos)
Ow_message = main_Font.render(f'{Owens}', False, "black")
Ow_message = pygame.transform.scale2x((Ow_message))
Tow_rect = butt_surf.get_rect(center=TOwpos)

TCC_message = main_Font.render(f'{CheffPrice}$', False, "black")
TCC_message = pygame.transform.scale2x((TCC_message))

TCCU_message = main_Font.render(f'{CurrsorPrice}$', False, "black")
TCCU_message = pygame.transform.scale2x((TCCU_message))

TCP_message = main_Font.render(f'{Plow_price}$', False, "black")
TCP_message = pygame.transform.scale2x((TCP_message))

TCO_message = main_Font.render(f'{Owen_Price}$', False, "black")
TCO_message = pygame.transform.scale2x((TCO_message))

TCR_message = main_Font.render(f'{ReviewPrice}$', False, "black")
TCR_message = pygame.transform.scale2x((TCR_message))


def is_over(rect, pos):
    return True if rect.collidepoint(pos[0], pos[1]) else False

#
Click_Event = pygame.USEREVENT + 1
pygame.time.set_timer(Click_Event,2000)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN and pygame.mouse.get_pressed()[0] == 1 and Hold == False:
            if is_over(butt_rect, mpos):
                print(clicks)
                clicks = clicks + additional_Click
                Click_message = main_Font.render(f'{clicks}', False, "black")
                Click_message = pygame.transform.scale2x((Click_message))
                Clicks_rect = Click_message.get_rect(center=BTpos)

            elif is_over(cheff_rect, mpos) and clicks >= CheffPrice:
                print(cheffs)
                clicks = clicks - CheffPrice
                CheffPrice = CheffPrice + 100
                cheffs = cheffs + 1
                cheffs_message = main_Font.render(f'{cheffs}', False, "black")
                TCC_message = main_Font.render(f'{CheffPrice}' + "$", False, "black")
                TCC_message = pygame.transform.scale2x((TCC_message))
                Click_message = main_Font.render(f'{clicks}', False, "black")
                Click_message = pygame.transform.scale2x((Click_message))
                cheffs_message = pygame.transform.scale2x((cheffs_message))
                Tcheff_rect = butt_surf.get_rect(center=TCpos)
                print(Tcheff_rect)

            elif is_over(curr_rect, mpos) and clicks >= CurrsorPrice:
                print(currsor)
                clicks = clicks - CurrsorPrice
                CurrsorPrice = CurrsorPrice + 25
                currsor = currsor + 1
                currsor_message = main_Font.render(f'{currsor}', False, "black")
                TCCU_message = main_Font.render(f'{CurrsorPrice}$', False, "black")
                TCCU_message = pygame.transform.scale2x((TCCU_message))
                Click_message = main_Font.render(f'{clicks}', False, "black")
                Click_message = pygame.transform.scale2x((Click_message))
                currsor_message = pygame.transform.scale2x((currsor_message))
                Tcurr_rect = butt_surf.get_rect(center=TCurrpos)

            elif is_over(plow_rect, mpos) and clicks >= Plow_price:
                print(Plows)
                clicks = clicks - Plow_price
                Plows = Plows + 1
                Plow_price = Plow_price + 50
                additional_Click = additional_Click + 1
                plow_message = main_Font.render(f'{Plows}', False, "black")
                TCP_message = main_Font.render(f'{Plow_price}$', False, "black")
                TCP_message = pygame.transform.scale2x((TCP_message))
                Click_message = main_Font.render(f'{clicks}', False, "black")
                Click_message = pygame.transform.scale2x((Click_message))
                plow_message = pygame.transform.scale2x((plow_message))
                Tpow_rect = butt_surf.get_rect(center=TPlowpos)

            elif is_over(Ow_rect, mpos) and clicks >= Owen_Price:
                print(Owens)
                clicks = clicks - Owen_Price
                Owen_Price = Owen_Price +75
                Owens = Owens + 1
                additional_Click = additional_Click + 2
                Ow_message = main_Font.render(f'{Owens}', False, "black")
                TCO_message = main_Font.render(f'{Owen_Price}$', False, "black")
                TCO_message = pygame.transform.scale2x((TCO_message))
                Click_message = main_Font.render(f'{clicks}', False, "black")
                Click_message = pygame.transform.scale2x((Click_message))
                Ow_message = pygame.transform.scale2x((Ow_message))
                Tow_rect = butt_surf.get_rect(center=TOwpos)

            elif is_over(rew_rect, mpos) and clicks >= ReviewPrice:
                print(Rewievs)
                Rewievs = Rewievs + 1
                clicks = clicks - ReviewPrice
                ReviewPrice = ReviewPrice + 125
                additional_Click = additional_Click + 5
                Rew_message = main_Font.render(f'{Rewievs}', False, "black")
                TCR_message = main_Font.render(f'{ReviewPrice}$', False, "black")
                TCR_message = pygame.transform.scale2x((TCR_message))
                Click_message = main_Font.render(f'{clicks}', False, "black")
                Click_message = pygame.transform.scale2x((Click_message))
                Rew_message = pygame.transform.scale2x((Rew_message))
                Trew_rect = butt_surf.get_rect(center=TRewpos)

        elif event.type == Click_Event:
            for i in range (currsor):
                clicks = clicks + 1
                Click_message = main_Font.render(f'{clicks}', False, "black")
                Click_message = pygame.transform.scale2x((Click_message))
                Clicks_rect = Click_message.get_rect(center=BTpos)
                print(currsor)
            for i in range (cheffs):
                clicks = clicks + 4
                Click_message = main_Font.render(f'{clicks}', False, "black")
                Click_message = pygame.transform.scale2x((Click_message))
                Clicks_rect = Click_message.get_rect(center=BTpos)
                print(currsor)
        elif  event.type == pygame.KEYDOWN and event.key == pygame.K_h and event.key == pygame.K_o and event.key == pygame.K_l and event.key == pygame.K_d:
            Hold = True
            print(Hold)
        elif  event.type == pygame.KEYDOWN and event.key == pygame.K_h and event.key == pygame.K_o and event.key == pygame.K_l and event.key == pygame.K_d and event.key == pygame.K_n:
            Hold = False
            print(Hold)

    Click_message = main_Font.render(f'{clicks}$', False, "black")
    Click_message = pygame.transform.scale2x((Click_message))
    Clicks_rect = Click_message.get_rect(center=BTpos)
    mpos = pygame.mouse.get_pos()

    if Hold:
        if is_over(butt_rect,mpos):
            if pygame.mouse.get_pressed()[0] == 1:
                print(clicks)
                clicks = clicks + additional_Click
                Click_message = main_Font.render(f'{clicks}', False, "black")
                Click_message = pygame.transform.scale2x((Click_message))

    screen.fill("grey")
    screen.blit(butt_surf,butt_rect)
    screen.blit(Click_message,Clicks_rect)

    screen.blit(cheff_surf, cheff_rect)
    screen.blit(cheffs_message, Tcheff_rect)

    screen.blit(curr_surf,curr_rect)
    screen.blit(currsor_message, Tcurr_rect)

    screen.blit(plow_surf,plow_rect)
    screen.blit(plow_message, Tpow_rect)

    screen.blit(rew_surf,rew_rect)
    screen.blit(Rew_message, Trew_rect)

    screen.blit(Ow_surf,Ow_rect)
    screen.blit(Ow_message, Tow_rect)

    screen.blit(TCC_message,TCC_rect)
    screen.blit(TCCU_message,TCCU_rect)
    screen.blit(TCP_message,TCP_rect)
    screen.blit(TCR_message,TCR_rect)
    screen.blit(TCO_message,TCO_rect)


    pygame.display.update()
    clock.tick(60)
