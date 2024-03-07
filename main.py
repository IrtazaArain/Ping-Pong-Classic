def main_loop():

    from game import Game

    g = Game()
    
    while g.running:
        g.curr_menu.interface()
        g.game_loop()

if __name__ == "__main__":
    main_loop()
