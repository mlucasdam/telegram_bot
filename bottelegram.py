# Importações de bibliotecas
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.remote.webdriver import By
from time import sleep
import requests

class MensagemPadrao:
    # Mensagens Padrão
    @staticmethod
    def mensagens():
        analise = '🤔📈🚀Coletando informações🤑💰'
        win = '🤑💰🎉🟩🎰 Green do Double 🎰🟩🎉🤑💰'
        win_branco = '🤑💰🎉⬜🎰 Green do branco 🎰⬜🎉💰🤑'
        loss = 'Essa não deu😭\nAguarde o proximo sinal e jogue conosco novamente🎰🟩🎉🤑💰'
        nao_confirmacao = 'Essa não deu😭\nAguarde o proximo sinal e jogue conosco novamente🎰🎉🤑💰'
        encerrando = '🟥🤖Robozinho da blaze doubles se despedindo, até a proxima!!!🟥🤖'
        txt = '🟩🤖Robozinho da blaze doubles iniciando🤖🟩\nLigando a maquina de fazer dinheiro💰🤑🔥🚀'
        txt_afirmativo = '🤔📈🚀Padrão encontrado, Analisando possibilidades🤑💰'
        
        msg = [analise, win, win_branco, loss, nao_confirmacao, encerrando, txt, txt_afirmativo]

        return msg


class bot_blaze:
    # Função para enviar mensagem para o Telegram
    def enviar_mensagem_free(self, mensagem):
        self.bot_token = '6478057231:AAHBb4hamW_b62xtR85M7o8ZJcqGGYbCD7Q'
        self.chat_id = '-1001956515529'
        self.url_blaze = '🎰 [Blaze](https://blaze.com/pt/games/double)'
        self.url = f'https://api.telegram.org/bot{self.bot_token}/sendMessage?chat_id={self.chat_id}&text={mensagem}\n{self.url_blaze}&parse_mode=Markdown'
        requests.get(self.url)

    # Função para enviar mensagem para o Telegram
    def enviar_mensagem(self, mensagem):
        self.bot_token = '6550070547:AAHCFRIKPuZcNAIQTIUuxif8pNXzW-pXWis'
        self.chat_id = '-1002008305971'
        self.url_blaze = '🎰 [Blaze](https://blaze.com/pt/games/double)'
        self.url = f'https://api.telegram.org/bot{self.bot_token}/sendMessage?chat_id={self.chat_id}&text={mensagem}\n{self.url_blaze}&parse_mode=Markdown'
        requests.get(self.url)
    
    # Função para configuração inicial do navegador
    def _init__(self):
        self.driver = uc.Chrome()
        self.driver.get('https://blaze.com/pt/games/double')

        mensagem_padrao = MensagemPadrao()
        self.msg = mensagem_padrao.mensagens() 

        self.cor = ['Branco','Preto','Vermelho']
        self.simbolo = ['⬜','⬛','🟥']

        print(self.msg[6])
        self.enviar_mensagem_free(self.msg[6])
        self.enviar_mensagem(self.msg[6])
    
    #Verificador de quantidade de sinais enviados
    def verifica_limite(self):
        self.contador = 0
        self.limite = 1

        return self.contador == self.limite

    # Função para aguardar a presença de um elemento na página
    def esperar(self):
        while True:
            try:
                self.driver.find_element(By.CLASS_NAME, 'time-left').find_element(By.TAG_NAME, 'span').text
                break
            except:
                pass
        
        while True:
            try:
                self.driver.find_element(By.CLASS_NAME, 'time-left').find_element(By.TAG_NAME, 'span').text
            except:
                break

    # Função para retornar o histórico de cores do jogo
    def retornar_historico(self):
        return [i['color'] for i in requests.get('https://blaze.com/api/roulette_games/recent').json()][::-1]

    # Função para retornar a cor mais recente do jogo
    def retornar_ultimo(self):
        return requests.get('https://blaze.com/api/roulette_games/current').json()['color']

    # Função para realizar a estratégia de Martingale
    def martin_gale(self, gale, ultimo):
        self.enviar_mensagem(gale)
        self.esperar()
        sleep(1.5)
        ultimo_ = self.retornar_ultimo()

        if ultimo_ != ultimo and ultimo_ != 0:
            self.enviar_mensagem(self.msg[1])
            return True
        
        elif ultimo_ == 0: 
            self.enviar_mensagem(self.msg[2])
            return True

    #Função que envia sinal
    def envia_sinal(self):
        while True:
            try:
                if self.verifica_limite():
                    self.enviar_mensagem(self.mensagem.msg[5])
                    sleep(1.5)
                    break

                else:
                    print('Esperando padrão....')
                    self.esperar()
                    sleep(1.5)

                    historico = self.retornar_historico()
                    ultimo = self.retornar_ultimo()
                    historico.append(ultimo)
                    padrao = historico[-4:]

                    mensagem = ''
                    mensagem += ''.join(self.simbolo[num] for num in padrao)

                    print(padrao)
                    self.enviar_mensagem(self.msg[0])

                    confirmacao = f'💎🤑💰\nConfirme a entrada no:\n{self.simbolo[padrao[0]]}{self.cor[padrao[0]]}\n{self.simbolo[0]} Proteção no branco\n💎🤑💰'

                    gale1 = f'Processando dados do algoritimo🔥🚀\n💎🤑💰Sinal Gerado💎🤑💰{self.simbolo[padrao[0]]} {self.cor[padrao[0]]}\n{self.simbolo[0]} Proteção no Branco\n💎🤑💰'
                    gale2 = f'Processando dados do algoritimo🔥🚀\n💎🤑💰Sinal Gerado💎🤑💰{self.simbolo[padrao[0]]} {self.cor[padrao[0]]}\n{self.simbolo[0]} Proteção no Branco\n💎🤑💰'

                    # Verifica padrões específicos para enviar mensagem de análise
                    if padrao in ([1,1,1,1], [2,2,2,2], [1,2,1,2], [2,1,2,1]):
                        self.enviar_mensagem_free(self.msg[7])
                        self.enviar_mensagem(self.msg[7])

                        self.esperar()
                        sleep(1.5)
                        ultimo = self.retornar_ultimo()

                        while True:
                            if ultimo == padrao[0]:
                                self.enviar_mensagem_free(confirmacao)
                                self.enviar_mensagem(confirmacao)

                                self.esperar()
                                sleep(1.5)
                                ultimo_ = self.retornar_ultimo()

                                if ultimo_ != ultimo and ultimo_ != 0:
                                    self.enviar_mensagem_free(self.msg[1])
                                    self.enviar_mensagem(self.msg[1])
                                    self.contador += 1
                                    break

                                elif ultimo_ == 0:
                                    self.enviar_mensagem_free(self.msg[3])
                                    self.enviar_mensagem(self.msg[3])
                                    self.contador += 1
                                    break

                                else:
                                    if self.martin_gale(gale1, ultimo):
                                        break

                                    else:
                                        if self.martin_gale(gale2, ultimo):
                                            break

                                        else:
                                            self.enviar_mensagem_free(self.msg[3])
                                            self.enviar_mensagem(self.msg[3])
                                            self.contador += 1
                                            break
                            else:
                                self.enviar_mensagem_free(self.msg[4])
                                self.enviar_mensagem(self.msg[4])
                                break
                    else:
                        sleep(1.5)

                        print(f'Não foi possivel chegar a uma conclusão🤔\nO ultimo padrão foi {mensagem}')
                        self.enviar_mensagem(f'Não foi possivel chegar a uma conclusão🤔\nO ultimo padrão foi {mensagem}')

            except Exception as e:
                print(e)
                self.driver.get('https://blaze.com/pt/games/double')
                sleep(10)
                pass

if __name__ == "__main__":
    bot = bot_blaze()
    bot._init__()
    bot.envia_sinal()