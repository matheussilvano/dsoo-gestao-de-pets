import pygame
import sys
from registry.registry import dono_controller, pet_controller, produto_controller, servico_controller, agendamento_controller, venda_controller, relatorio_controller, despesa_controller
import datetime

MENU_OPCOES = [
    ("Vendas", "vendas"),
    ("Agendamento", "agendamento"),
    ("Donos", "donos"),
    ("Pets", "pets"),
    ("Produtos", "produtos"),
    ("Serviços", "servicos"),
    ("Relatórios", "relatorios"),
    ("Sair", "sair")
]

RELATORIOS_OPCOES = [
    ("Relatório Geral de Vendas", "geral_vendas"),
    ("Ranking de Donos por Gasto", "donos_gasto"),
    ("Ranking de Pets por Vendas", "pets_vendas"),
    ("Produtos Mais Usados", "produtos_usados"),
    ("Serviços Mais Vendidos", "servicos_vendidos"),
    ("Voltar", "voltar")
]

class PygameView:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Petshop - Interface Gráfica')
        self.font = pygame.font.SysFont(None, 36)
        self.small_font = pygame.font.SysFont(None, 28)
        self.clock = pygame.time.Clock()
        self.tela_atual = self.menu_principal
        self.dono_selecionado = None
        self.pet_selecionado = None
        self.produto_selecionado = None
        self.servico_selecionado = None
        self.agendamento_selecionado = None
        self.venda_selecionada = None

    def executar(self):
        while True:
            self.tela_atual()

    def menu_principal(self):
        rodando = True
        while rodando:
            self.screen.fill((255, 255, 255))
            titulo = self.font.render('Menu Principal', True, (0, 0, 0))
            self.screen.blit(titulo, (300, 40))
            mouse_pos = pygame.mouse.get_pos()
            botoes = []
            for i, (texto, acao) in enumerate(MENU_OPCOES):
                rect = pygame.Rect(270, 100 + i*60, 260, 50)
                cor = (200, 200, 200) if rect.collidepoint(mouse_pos) else (220, 220, 220)
                pygame.draw.rect(self.screen, cor, rect)
                label = self.small_font.render(texto, True, (0, 0, 0))
                self.screen.blit(label, (rect.x + 20, rect.y + 12))
                botoes.append((rect, acao))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                    
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return
                    
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for rect, acao in botoes:
                        if rect.collidepoint(event.pos):
                            if acao == "sair":
                                pygame.quit()
                                sys.exit()
                                return
                                
                            elif acao == "donos":
                                self.tela_atual = self.tela_listar_donos
                                return
                            elif acao == "pets":
                                self.tela_atual = self.tela_listar_pets
                                return
                            elif acao == "produtos":
                                self.tela_atual = self.tela_listar_produtos
                                return
                            elif acao == "servicos":
                                self.tela_atual = self.tela_listar_servicos
                                return
                            elif acao == "agendamento":
                                self.tela_atual = self.tela_listar_agendamentos
                                return
                            elif acao == "vendas":
                                self.tela_atual = self.tela_listar_vendas
                                return
                            elif acao == "relatorios":
                                self.tela_atual = self.menu_relatorios
                                return
                            else:
                                self.tela_atual = lambda: self.tela_stub(acao)
                                return
            self.clock.tick(60)

    def menu_relatorios(self):
        rodando = True
        while rodando:
            self.screen.fill((240, 240, 255))
            titulo = self.font.render('Menu de Relatórios', True, (0, 0, 0))
            self.screen.blit(titulo, (270, 40))
            mouse_pos = pygame.mouse.get_pos()
            botoes = []
            for i, (texto, acao) in enumerate(RELATORIOS_OPCOES):
                rect = pygame.Rect(220, 100 + i * 60, 360, 50)
                cor = (200, 200, 200) if rect.collidepoint(mouse_pos) else (220, 220, 220)
                pygame.draw.rect(self.screen, cor, rect)
                label = self.small_font.render(texto, True, (0, 0, 0))
                self.screen.blit(label, (rect.x + 20, rect.y + 12))
                botoes.append((rect, acao))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                    
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.tela_atual = self.menu_principal
                    return
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for rect, acao in botoes:
                        if rect.collidepoint(event.pos):
                            if acao == "voltar":
                                self.tela_atual = self.menu_principal
                                return
                            elif acao == "geral_vendas":
                                self.tela_atual = self.tela_relatorio_geral_vendas
                                return
                            elif acao == "donos_gasto":
                                self.tela_atual = self.tela_relatorio_donos_por_gasto
                                return
                            elif acao == "pets_vendas":
                                self.tela_atual = self.tela_relatorio_pets_por_vendas
                                return
                            elif acao == "produtos_usados":
                                self.tela_atual = self.tela_relatorio_produtos_mais_usados
                                return
                            elif acao == "servicos_vendidos":
                                self.tela_atual = self.tela_relatorio_servicos_mais_vendidos
                                return
            self.clock.tick(60)

    def tela_listar_donos(self):
        rodando = True
        scroll = 0
        try:
            donos = dono_controller.listar_donos()
        except Exception as e:
            self._mostrar_erro_pygame(f"Erro ao listar donos: {e}")
            donos = []
        selecionado = None
        while rodando:
            self.screen.fill((245, 245, 245))
            titulo = self.font.render('Donos cadastrados', True, (0, 0, 0))
            self.screen.blit(titulo, (40, 30))
            rect_add = pygame.Rect(600, 30, 160, 40)
            pygame.draw.rect(self.screen, (180, 255, 180), rect_add)
            self.screen.blit(self.small_font.render('Adicionar', True, (0,0,0)), (rect_add.x+30, rect_add.y+7))
            y = 90 - scroll
            mouse_pos = pygame.mouse.get_pos()
            rects_donos = []
            botoes_editar = []
            botoes_excluir = []
            for idx, dono in enumerate(donos, 1):
                nome = getattr(dono, 'nome', str(dono))
                telefone = getattr(dono, 'telefone', '')
                texto = f"{idx}. {nome} - {telefone}"
                if len(texto) > 38:
                    texto = texto[:35] + '...'
                label = self.small_font.render(texto, True, (30, 30, 30))
                rect = label.get_rect(topleft=(60, y))
                self.screen.blit(label, rect.topleft)
                rects_donos.append((rect, dono))
                rect_editar = pygame.Rect(500, y, 80, 30)
                pygame.draw.rect(self.screen, (255, 255, 180), rect_editar)
                self.screen.blit(self.small_font.render('Editar', True, (0,0,0)), (rect_editar.x+10, rect_editar.y+5))
                botoes_editar.append((rect_editar, dono))
                rect_excluir = pygame.Rect(600, y, 80, 30)
                pygame.draw.rect(self.screen, (255, 180, 180), rect_excluir)
                self.screen.blit(self.small_font.render('Excluir', True, (0,0,0)), (rect_excluir.x+10, rect_excluir.y+5))
                botoes_excluir.append((rect_excluir, dono))
                y += 45 
            rect_voltar = pygame.Rect(20, 540, 120, 40)
            pygame.draw.rect(self.screen, (200, 200, 200), rect_voltar)
            label_voltar = self.small_font.render('Voltar', True, (0, 0, 0))
            self.screen.blit(label_voltar, (rect_voltar.x + 20, rect_voltar.y + 7))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.tela_atual = self.menu_principal
                        return
                    if event.key == pygame.K_DOWN:
                        scroll += 45
                    if event.key == pygame.K_UP and scroll > 0:
                        scroll -= 45
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for rect, dono in botoes_editar:
                        if rect.collidepoint(event.pos):
                            self.dono_selecionado = dono
                            self.tela_atual = self.tela_editar_dono
                            return
                    for rect, dono in botoes_excluir:
                        if rect.collidepoint(event.pos):
                            self.dono_selecionado = dono
                            self.tela_atual = self.tela_excluir_dono
                            return
                    if rect_add.collidepoint(event.pos):
                        self.tela_atual = self.tela_adicionar_dono
                        return
                    if rect_voltar.collidepoint(event.pos):
                        self.tela_atual = self.menu_principal
                        return
            self.clock.tick(60)

    def _mostrar_erro_pygame(self, mensagem):
        rodando = True
        while rodando:
            self.screen.fill((255, 220, 220))
            erro_label = self.font.render('Erro', True, (180,0,0))
            self.screen.blit(erro_label, (350, 200))
            msg = self.small_font.render(mensagem, True, (120,0,0))
            self.screen.blit(msg, (100, 300))
            ok_rect = pygame.Rect(350, 400, 100, 40)
            pygame.draw.rect(self.screen, (255,180,180), ok_rect)
            self.screen.blit(self.small_font.render('OK', True, (0,0,0)), (ok_rect.x+25, ok_rect.y+7))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                    
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if ok_rect.collidepoint(event.pos):
                        rodando = False
                        return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    rodando = False
                    return

    def tela_adicionar_dono(self):
        self._tela_form_dono('Adicionar Dono')

    def tela_editar_dono(self):
        self._tela_form_dono('Editar Dono', self.dono_selecionado)

    def tela_excluir_dono(self):
        try:
            dono = self.dono_selecionado
            if not dono:
                self.tela_atual = self.tela_listar_donos
                return
            rodando = True
            erro_msg = ''
            while rodando:
                self.screen.fill((255, 230, 230))
                t = self.font.render('Excluir Dono', True, (180,0,0))
                self.screen.blit(t, (220, 40))
                label = self.small_font.render(f"Tem certeza que deseja excluir '{getattr(dono, 'nome', '')}'?", True, (0,0,0))
                self.screen.blit(label, (120, 120))
                rect_sim = pygame.Rect(250, 200, 120, 40)
                rect_nao = pygame.Rect(400, 200, 120, 40)
                pygame.draw.rect(self.screen, (255,180,180), rect_sim)
                pygame.draw.rect(self.screen, (200,200,200), rect_nao)
                self.screen.blit(self.small_font.render('Sim', True, (0,0,0)), (rect_sim.x+30, rect_sim.y+7))
                self.screen.blit(self.small_font.render('Não', True, (0,0,0)), (rect_nao.x+30, rect_nao.y+7))
                if erro_msg:
                    pygame.draw.rect(self.screen, (255,220,220), (180, 300, 440, 50))
                    err_label = self.small_font.render(erro_msg, True, (180,0,0))
                    self.screen.blit(err_label, (200, 315))
                    ok_rect = pygame.Rect(570, 310, 40, 30)
                    pygame.draw.rect(self.screen, (255,180,180), ok_rect)
                    self.screen.blit(self.small_font.render('OK', True, (0,0,0)), (ok_rect.x+5, ok_rect.y+5))
                pygame.display.flip()
                for event in pygame.event.get():
                    if erro_msg:
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            if ok_rect.collidepoint(event.pos):
                                erro_msg = ''
                        continue
                    if event.type == pygame.QUIT:
                        return
                        
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.tela_atual = self.tela_listar_donos
                            return
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if rect_sim.collidepoint(event.pos):
                            try:
                                if hasattr(dono, 'nome') and dono_controller.excluir_dono(dono.nome):
                                    self.tela_atual = self.tela_listar_donos
                                    return
                                else:
                                    erro_msg = 'Erro ao excluir dono.'
                            except Exception as e:
                                erro_msg = str(e)
                        if rect_nao.collidepoint(event.pos):
                            self.tela_atual = self.tela_listar_donos
                            return
        except Exception as e:
            self._mostrar_erro_pygame(f"Erro ao excluir dono: {e}")

    def _tela_form_dono(self, titulo, dono=None):
        rodando = True
        nome = dono.nome if dono else ''
        telefone = dono.telefone if dono else ''
        endereco = dono.endereco if dono else ''
        campo = 0 
        campos = [nome, telefone, endereco]
        erro_msg = ''
        pygame.key.start_text_input()
        while rodando:
            self.screen.fill((220, 240, 255))
            t = self.font.render(titulo, True, (0,0,0))
            self.screen.blit(t, (220, 40))
            labels = ['Nome:', 'Telefone:', 'Endereço:']
            for i, label in enumerate(labels):
                cor = (0,0,180) if campo == i else (0,0,0)
                l = self.small_font.render(label, True, cor)
                self.screen.blit(l, (120, 120 + i*60))
                pygame.draw.rect(self.screen, (255,255,255), (250, 115 + i*60, 350, 40))
                valor = self.small_font.render(campos[i], True, (0,0,0))
                self.screen.blit(valor, (260, 125 + i*60))

            rect_salvar = pygame.Rect(250, 350, 120, 40)
            rect_cancelar = pygame.Rect(400, 350, 120, 40)
            pygame.draw.rect(self.screen, (180,255,180), rect_salvar)
            pygame.draw.rect(self.screen, (200,200,200), rect_cancelar)
            self.screen.blit(self.small_font.render('Salvar', True, (0,0,0)), (rect_salvar.x+20, rect_salvar.y+7))
            self.screen.blit(self.small_font.render('Cancelar', True, (0,0,0)), (rect_cancelar.x+20, rect_cancelar.y+7))
            if erro_msg:
                pygame.draw.rect(self.screen, (255,220,220), (180, 420, 440, 50))
                err_label = self.small_font.render(erro_msg, True, (180,0,0))
                self.screen.blit(err_label, (200, 435))
                ok_rect = pygame.Rect(570, 430, 40, 30)
                pygame.draw.rect(self.screen, (255,180,180), ok_rect)
                self.screen.blit(self.small_font.render('OK', True, (0,0,0)), (ok_rect.x+5, ok_rect.y+5))
            pygame.display.flip()
            for event in pygame.event.get():
                if erro_msg:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if ok_rect.collidepoint(event.pos):
                            erro_msg = ''
                    continue
                if event.type == pygame.QUIT:
                    pygame.key.stop_text_input()
                    return
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.key.stop_text_input()
                        self.tela_atual = self.tela_listar_donos
                        return
                    if event.key == pygame.K_TAB:
                        campo = (campo + 1) % 3
                    elif event.key == pygame.K_BACKSPACE:
                        if len(campos[campo]) > 0:
                            campos[campo] = campos[campo][:-1]
                    elif event.key == pygame.K_RETURN:
                        try:
                            if not campos[0]:
                                raise ValueError('Nome obrigatório')
                            if not campos[1]:
                                raise ValueError('Telefone obrigatório')
                            if not campos[2]:
                                raise ValueError('Endereço obrigatório')
                            if dono:
                                dono_controller.atualizar_dono(dono.nome, nome=campos[0], telefone=campos[1], endereco=campos[2])
                            else:
                                dono_controller.criar_dono(campos[0], campos[1], campos[2])
                            pygame.key.stop_text_input()
                            self.tela_atual = self.tela_listar_donos
                            return
                        except Exception as e:
                            erro_msg = str(e)
                    elif event.unicode and len(event.unicode) == 1 and not event.key in [pygame.K_TAB, pygame.K_RETURN, pygame.K_ESCAPE, pygame.K_BACKSPACE]:
                        campos[campo] += event.unicode
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if rect_salvar.collidepoint(event.pos):
                        try:
                            if not campos[0]:
                                raise ValueError('Nome obrigatório')
                            if not campos[1]:
                                raise ValueError('Telefone obrigatório')
                            if not campos[2]:
                                raise ValueError('Endereço obrigatório')
                            if dono:
                                dono_controller.atualizar_dono(dono.nome, nome=campos[0], telefone=campos[1], endereco=campos[2])
                            else:
                                dono_controller.criar_dono(campos[0], campos[1], campos[2])
                            pygame.key.stop_text_input()
                            self.tela_atual = self.tela_listar_donos
                            return
                        except Exception as e:
                            erro_msg = str(e)
                    if rect_cancelar.collidepoint(event.pos):
                        pygame.key.stop_text_input()
                        self.tela_atual = self.tela_listar_donos
                        return
            self.clock.tick(60)
        pygame.key.stop_text_input()

    def tela_listar_pets(self):
        rodando = True
        scroll = 0
        try:
            pets = pet_controller.listar_pets()
        except Exception as e:
            self._mostrar_erro_pygame(f"Erro ao listar pets: {e}")
            pets = []
        while rodando:
            self.screen.fill((245, 245, 245))
            titulo = self.font.render('Pets cadastrados', True, (0, 0, 0))
            self.screen.blit(titulo, (40, 30))

            rect_add = pygame.Rect(600, 30, 160, 40)
            pygame.draw.rect(self.screen, (180, 255, 180), rect_add)
            self.screen.blit(self.small_font.render('Adicionar', True, (0,0,0)), (rect_add.x+30, rect_add.y+7))
            y = 90 - scroll
            mouse_pos = pygame.mouse.get_pos()
            botoes_editar = []
            botoes_excluir = []
            for idx, pet in enumerate(pets, 1):
                nome = getattr(pet, 'nome', str(pet))
                dono_nome = getattr(pet.dono, 'nome', '')
                idade = getattr(pet, 'idade', '')
                texto = f"{idx}. {nome} - {dono_nome} - {idade} anos"
                if len(texto) > 38:
                    texto = texto[:35] + '...'
                label = self.small_font.render(texto, True, (30, 30, 30))
                rect = label.get_rect(topleft=(60, y))
                self.screen.blit(label, rect.topleft)

                rect_editar = pygame.Rect(500, y, 80, 30)
                pygame.draw.rect(self.screen, (255, 255, 180), rect_editar)
                self.screen.blit(self.small_font.render('Editar', True, (0,0,0)), (rect_editar.x+10, rect_editar.y+5))
                botoes_editar.append((rect_editar, pet))

                rect_excluir = pygame.Rect(600, y, 80, 30)
                pygame.draw.rect(self.screen, (255, 180, 180), rect_excluir)
                self.screen.blit(self.small_font.render('Excluir', True, (0,0,0)), (rect_excluir.x+10, rect_excluir.y+5))
                botoes_excluir.append((rect_excluir, pet))
                y += 45

            rect_voltar = pygame.Rect(20, 540, 120, 40)
            pygame.draw.rect(self.screen, (200, 200, 200), rect_voltar)
            label_voltar = self.small_font.render('Voltar', True, (0, 0, 0))
            self.screen.blit(label_voltar, (rect_voltar.x + 20, rect_voltar.y + 7))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.tela_atual = self.menu_principal
                        return
                    if event.key == pygame.K_DOWN:
                        scroll += 45
                    if event.key == pygame.K_UP and scroll > 0:
                        scroll -= 45
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for rect, pet in botoes_editar:
                        if rect.collidepoint(event.pos):
                            self.pet_selecionado = pet
                            self.tela_atual = self.tela_editar_pet
                            return
                    for rect, pet in botoes_excluir:
                        if rect.collidepoint(event.pos):
                            self.pet_selecionado = pet
                            self.tela_atual = self.tela_excluir_pet
                            return
                    if rect_add.collidepoint(event.pos):
                        self.tela_atual = self.tela_adicionar_pet
                        return
                    if rect_voltar.collidepoint(event.pos):
                        self.tela_atual = self.menu_principal
                        return
            self.clock.tick(60)

    def tela_adicionar_pet(self):
        self._tela_form_pet('Adicionar Pet')

    def tela_editar_pet(self):
        self._tela_form_pet('Editar Pet', self.pet_selecionado)

    def tela_excluir_pet(self):
        rodando = True
        while rodando:
            self.screen.fill((255, 220, 220))
            msg = self.font.render(f'Excluir pet?', True, (120,0,0))
            self.screen.blit(msg, (250, 150))
            nome = str(self.pet_selecionado)
            label_nome = self.small_font.render(nome, True, (0,0,0))
            self.screen.blit(label_nome, (250, 200))
            rect_confirma = pygame.Rect(250, 300, 120, 40)
            rect_cancela = pygame.Rect(400, 300, 120, 40)
            pygame.draw.rect(self.screen, (255,180,180), rect_confirma)
            pygame.draw.rect(self.screen, (200,200,200), rect_cancela)
            self.screen.blit(self.small_font.render('Confirmar', True, (0,0,0)), (rect_confirma.x+10, rect_confirma.y+7))
            self.screen.blit(self.small_font.render('Cancelar', True, (0,0,0)), (rect_cancela.x+10, rect_cancela.y+7))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                    
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.tela_atual = self.tela_listar_pets
                    return
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if rect_confirma.collidepoint(event.pos):
                        pet_controller.excluir_pet(self.pet_selecionado.nome)
                        self.tela_atual = self.tela_listar_pets
                        return
                    if rect_cancela.collidepoint(event.pos):
                        self.tela_atual = self.tela_listar_pets
                        return
            self.clock.tick(60)

    def _tela_form_pet(self, titulo, pet=None):
        rodando = True
        nome = pet.nome if pet else ''
        especie = pet.especie if pet else ''
        raca = pet.raca if pet else ''
        idade = str(pet.idade) if pet else ''
        donos = dono_controller.listar_donos()
        dono_idx = donos.index(pet.dono) if pet and pet.dono in donos else 0
        campo = 0 
        campos = [nome, especie, raca, idade]
        erro_msg = ''
        pygame.key.start_text_input()
        while rodando:
            self.screen.fill((220, 240, 255))
            t = self.font.render(titulo, True, (0,0,0))
            self.screen.blit(t, (220, 40))
            labels = ['Nome:', 'Espécie:', 'Raça:', 'Idade:', 'Dono:']
            for i, label in enumerate(labels):
                cor = (0,0,180) if campo == i else (0,0,0)
                l = self.small_font.render(label, True, cor)
                self.screen.blit(l, (120, 120 + i*60))
                if i < 4:
                    pygame.draw.rect(self.screen, (255,255,255), (250, 115 + i*60, 350, 40))
                    valor = self.small_font.render(campos[i], True, (0,0,0))
                    self.screen.blit(valor, (260, 125 + i*60))
                else:
                    dono_nome = donos[dono_idx].nome if donos else 'Sem dono'
                    valor = self.small_font.render(dono_nome, True, (0,0,0))
                    self.screen.blit(valor, (260, 125 + i*60))

            rect_salvar = pygame.Rect(250, 420, 120, 40)
            rect_cancelar = pygame.Rect(400, 420, 120, 40)
            pygame.draw.rect(self.screen, (180,255,180), rect_salvar)
            pygame.draw.rect(self.screen, (200,200,200), rect_cancelar)
            self.screen.blit(self.small_font.render('Salvar', True, (0,0,0)), (rect_salvar.x+20, rect_salvar.y+7))
            self.screen.blit(self.small_font.render('Cancelar', True, (0,0,0)), (rect_cancelar.x+20, rect_cancelar.y+7))
            if erro_msg:
                pygame.draw.rect(self.screen, (255,220,220), (180, 490, 440, 50))
                err_label = self.small_font.render(erro_msg, True, (180,0,0))
                self.screen.blit(err_label, (200, 505))
                ok_rect = pygame.Rect(570, 500, 40, 30)
                pygame.draw.rect(self.screen, (255,180,180), ok_rect)
                self.screen.blit(self.small_font.render('OK', True, (0,0,0)), (ok_rect.x+5, ok_rect.y+5))
            pygame.display.flip()
            for event in pygame.event.get():
                if erro_msg:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if ok_rect.collidepoint(event.pos):
                            erro_msg = ''
                    continue
                if event.type == pygame.QUIT:
                    pygame.key.stop_text_input()
                    return
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.key.stop_text_input()
                        self.tela_atual = self.tela_listar_pets
                        return
                    if event.key == pygame.K_TAB:
                        campo = (campo + 1) % 5
                    elif event.key == pygame.K_BACKSPACE:
                        if campo < 4 and len(campos[campo]) > 0:
                            campos[campo] = campos[campo][:-1]
                    elif event.key == pygame.K_RETURN:
                        try:
                            if not campos[0]: raise ValueError('Nome obrigatório')
                            if not campos[1]: raise ValueError('Espécie obrigatória')
                            if not campos[2]: raise ValueError('Raça obrigatória')
                            if not campos[3]: raise ValueError('Idade obrigatória')
                            if not donos: raise ValueError('Dono obrigatório')
                            if pet:
                                pet_controller.atualizar_pet(pet.nome, nome=campos[0], especie=campos[1], raca=campos[2], idade=int(campos[3]))
                            else:
                                pet_controller.criar_pet(donos[dono_idx].nome, campos[0], campos[1], campos[2], int(campos[3]))
                            pygame.key.stop_text_input()
                            self.tela_atual = self.tela_listar_pets
                            return
                        except Exception as e:
                            erro_msg = str(e)
                    elif event.unicode and campo < 4 and len(event.unicode) == 1 and not event.key in [pygame.K_TAB, pygame.K_RETURN, pygame.K_ESCAPE, pygame.K_BACKSPACE]:
                        campos[campo] += event.unicode
                    elif campo == 4 and donos:
                        if event.key == pygame.K_LEFT and dono_idx > 0:
                            dono_idx -= 1
                        if event.key == pygame.K_RIGHT and dono_idx < len(donos)-1:
                            dono_idx += 1

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if rect_salvar.collidepoint(event.pos):
                        try:
                            if not campos[0]: raise ValueError('Nome obrigatório')
                            if not campos[1]: raise ValueError('Espécie obrigatória')
                            if not campos[2]: raise ValueError('Raça obrigatória')
                            if not campos[3]: raise ValueError('Idade obrigatória')
                            if not donos: raise ValueError('Dono obrigatório')
                            if pet:
                                pet_controller.atualizar_pet(pet.nome, nome=campos[0], especie=campos[1], raca=campos[2], idade=int(campos[3]))
                            else:
                                pet_controller.criar_pet(donos[dono_idx].nome, campos[0], campos[1], campos[2], int(campos[3]))
                            pygame.key.stop_text_input()
                            self.tela_atual = self.tela_listar_pets
                            return
                        except Exception as e:
                            erro_msg = str(e)
                    if rect_cancelar.collidepoint(event.pos):
                        pygame.key.stop_text_input()
                        self.tela_atual = self.tela_listar_pets
                        return
            self.clock.tick(60)
        pygame.key.stop_text_input()

    def tela_listar_produtos(self):
        rodando = True
        scroll = 0
        try:
            produtos = produto_controller.listar_produtos()
        except Exception as e:
            self._mostrar_erro_pygame(f"Erro ao listar produtos: {e}")
            produtos = []
        while rodando:
            self.screen.fill((245, 245, 245))
            titulo = self.font.render('Produtos cadastrados', True, (0, 0, 0))
            self.screen.blit(titulo, (40, 30))
            rect_add = pygame.Rect(600, 30, 160, 40)
            pygame.draw.rect(self.screen, (180, 255, 180), rect_add)
            self.screen.blit(self.small_font.render('Adicionar', True, (0,0,0)), (rect_add.x+30, rect_add.y+7))
            y = 90 - scroll
            botoes_editar = []
            botoes_excluir = []
            for idx, prod in enumerate(produtos, 1):
                nome = getattr(prod, 'nome', str(prod))
                custo = getattr(prod, 'custo_unitario', '')
                texto = f"{idx}. {nome} - R$ {custo:.2f}"
                if len(texto) > 38:
                    texto = texto[:35] + '...'
                label = self.small_font.render(texto, True, (30, 30, 30))
                rect = label.get_rect(topleft=(60, y))
                self.screen.blit(label, rect.topleft)
                rect_editar = pygame.Rect(500, y, 80, 30)
                pygame.draw.rect(self.screen, (255, 255, 180), rect_editar)
                self.screen.blit(self.small_font.render('Editar', True, (0,0,0)), (rect_editar.x+10, rect_editar.y+5))
                botoes_editar.append((rect_editar, prod))
                rect_excluir = pygame.Rect(600, y, 80, 30)
                pygame.draw.rect(self.screen, (255, 180, 180), rect_excluir)
                self.screen.blit(self.small_font.render('Excluir', True, (0,0,0)), (rect_excluir.x+10, rect_excluir.y+5))
                botoes_excluir.append((rect_excluir, prod))
                y += 45
            rect_voltar = pygame.Rect(20, 540, 120, 40)
            pygame.draw.rect(self.screen, (200, 200, 200), rect_voltar)
            label_voltar = self.small_font.render('Voltar', True, (0, 0, 0))
            self.screen.blit(label_voltar, (rect_voltar.x + 20, rect_voltar.y + 7))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.tela_atual = self.menu_principal
                        return
                    if event.key == pygame.K_DOWN:
                        scroll += 45
                    if event.key == pygame.K_UP and scroll > 0:
                        scroll -= 45
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for rect, prod in botoes_editar:
                        if rect.collidepoint(event.pos):
                            self.produto_selecionado = prod
                            self.tela_atual = self.tela_editar_produto
                            return
                    for rect, prod in botoes_excluir:
                        if rect.collidepoint(event.pos):
                            self.produto_selecionado = prod
                            self.tela_atual = self.tela_excluir_produto
                            return
                    if rect_add.collidepoint(event.pos):
                        self.tela_atual = self.tela_adicionar_produto
                        return
                    if rect_voltar.collidepoint(event.pos):
                        self.tela_atual = self.menu_principal
                        return
            self.clock.tick(60)

    def tela_adicionar_produto(self):
        self._tela_form_produto('Adicionar Produto')

    def tela_editar_produto(self):
        self._tela_form_produto('Editar Produto', self.produto_selecionado)

    def tela_excluir_produto(self):
        rodando = True
        while rodando:
            self.screen.fill((255, 220, 220))
            msg = self.font.render(f'Excluir produto?', True, (120,0,0))
            self.screen.blit(msg, (250, 150))
            nome = str(self.produto_selecionado)
            label_nome = self.small_font.render(nome, True, (0,0,0))
            self.screen.blit(label_nome, (250, 200))
            rect_confirma = pygame.Rect(250, 300, 120, 40)
            rect_cancela = pygame.Rect(400, 300, 120, 40)
            pygame.draw.rect(self.screen, (255,180,180), rect_confirma)
            pygame.draw.rect(self.screen, (200,200,200), rect_cancela)
            self.screen.blit(self.small_font.render('Confirmar', True, (0,0,0)), (rect_confirma.x+10, rect_confirma.y+7))
            self.screen.blit(self.small_font.render('Cancelar', True, (0,0,0)), (rect_cancela.x+10, rect_cancela.y+7))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                    
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.tela_atual = self.tela_listar_produtos
                    return
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if rect_confirma.collidepoint(event.pos):
                        produto_controller.excluir_produto(self.produto_selecionado.nome)
                        self.tela_atual = self.tela_listar_produtos
                        return
                    if rect_cancela.collidepoint(event.pos):
                        self.tela_atual = self.tela_listar_produtos
                        return
            self.clock.tick(60)

    def _tela_form_produto(self, titulo, prod=None):
        rodando = True
        nome = prod.nome if prod else ''
        quantidade = str(prod.quantidade_estoque) if prod else ''
        custo = str(prod.custo_unitario) if prod else ''
        campo = 0
        campos = [nome, quantidade, custo]
        erro_msg = ''
        pygame.key.start_text_input()
        while rodando:
            self.screen.fill((220, 240, 255))
            t = self.font.render(titulo, True, (0,0,0))
            self.screen.blit(t, (220, 40))
            labels = ['Nome:', 'Quantidade:', 'Custo unitário:']
            for i, label in enumerate(labels):
                cor = (0,0,180) if campo == i else (0,0,0)
                l = self.small_font.render(label, True, cor)
                self.screen.blit(l, (120, 120 + i*60))
                pygame.draw.rect(self.screen, (255,255,255), (300, 115 + i*60, 350, 40))
                valor = self.small_font.render(campos[i], True, (0,0,0))
                self.screen.blit(valor, (310, 125 + i*60))

            rect_salvar = pygame.Rect(250, 350, 120, 40)
            rect_cancelar = pygame.Rect(400, 350, 120, 40)
            pygame.draw.rect(self.screen, (180,255,180), rect_salvar)
            pygame.draw.rect(self.screen, (200,200,200), rect_cancelar)
            self.screen.blit(self.small_font.render('Salvar', True, (0,0,0)), (rect_salvar.x+20, rect_salvar.y+7))
            self.screen.blit(self.small_font.render('Cancelar', True, (0,0,0)), (rect_cancelar.x+20, rect_cancelar.y+7))
            
            if erro_msg:
                pygame.draw.rect(self.screen, (255,220,220), (180, 420, 440, 50))
                err_label = self.small_font.render(erro_msg, True, (180,0,0))
                self.screen.blit(err_label, (200, 435))
                ok_rect = pygame.Rect(570, 430, 40, 30)
                pygame.draw.rect(self.screen, (255,180,180), ok_rect)
                self.screen.blit(self.small_font.render('OK', True, (0,0,0)), (ok_rect.x+5, ok_rect.y+5))
            pygame.display.flip()

            for event in pygame.event.get():
                if erro_msg:
                    if event.type == pygame.MOUSEBUTTONDOWN and ok_rect.collidepoint(event.pos):
                        erro_msg = ''
                    continue

                def salvar_produto_logica():
                    nonlocal erro_msg
                    try:
                        if not campos[0]: raise ValueError('Nome obrigatório')
                        if not campos[1]: raise ValueError('Quantidade obrigatória')
                        if not campos[2]: raise ValueError('Custo unitário obrigatório')
                        qtd = int(campos[1])
                        custo_val = float(campos[2])
                        
                        if prod:
                            dados = {"nome": campos[0], "quantidade_estoque": qtd, "custo_unitario": custo_val}
                            produto_controller.atualizar_produto(prod.nome, **dados)
                        else:
                            produto_controller.criar_produto(campos[0], qtd, custo_val)
                        
                        pygame.key.stop_text_input()
                        self.tela_atual = self.tela_listar_produtos
                        return True
                    except Exception as e:
                        erro_msg = str(e)
                        return False

                if event.type == pygame.QUIT:
                    pygame.key.stop_text_input()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.key.stop_text_input()
                        self.tela_atual = self.tela_listar_produtos
                        return
                    if event.key == pygame.K_TAB:
                        campo = (campo + 1) % 3
                    elif event.key == pygame.K_BACKSPACE:
                        campos[campo] = campos[campo][:-1]
                    elif event.key == pygame.K_RETURN:
                        if salvar_produto_logica(): return
                    elif event.unicode and len(event.unicode) == 1:
                        campos[campo] += event.unicode
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if rect_salvar.collidepoint(event.pos):
                        if salvar_produto_logica(): return
                    if rect_cancelar.collidepoint(event.pos):
                        pygame.key.stop_text_input()
                        self.tela_atual = self.tela_listar_produtos
                        return
            self.clock.tick(60)
        pygame.key.stop_text_input()
        
    def tela_listar_servicos(self):
        rodando = True
        scroll = 0
        try:
            servicos = servico_controller.listar_servicos()
        except Exception as e:
            self._mostrar_erro_pygame(f"Erro ao listar serviços: {e}")
            servicos = []
        while rodando:
            self.screen.fill((245, 245, 245))
            titulo = self.font.render('Serviços cadastrados', True, (0, 0, 0))
            self.screen.blit(titulo, (40, 30))
            rect_add = pygame.Rect(600, 30, 160, 40)
            pygame.draw.rect(self.screen, (180, 255, 180), rect_add)
            self.screen.blit(self.small_font.render('Adicionar', True, (0,0,0)), (rect_add.x+30, rect_add.y+7))
            y = 90 - scroll
            botoes_editar = []
            botoes_excluir = []
            for idx, serv in enumerate(servicos, 1):
                nome = getattr(serv, 'nome', str(serv))
                preco = getattr(serv, 'preco', '')
                texto = f"{idx}. {nome} - R$ {preco:.2f}"
                if len(texto) > 38:
                    texto = texto[:35] + '...'
                label = self.small_font.render(texto, True, (30, 30, 30))
                rect = label.get_rect(topleft=(60, y))
                self.screen.blit(label, rect.topleft)
                rect_editar = pygame.Rect(500, y, 80, 30)
                pygame.draw.rect(self.screen, (255, 255, 180), rect_editar)
                self.screen.blit(self.small_font.render('Editar', True, (0,0,0)), (rect_editar.x+10, rect_editar.y+5))
                botoes_editar.append((rect_editar, serv))
                rect_excluir = pygame.Rect(600, y, 80, 30)
                pygame.draw.rect(self.screen, (255, 180, 180), rect_excluir)
                self.screen.blit(self.small_font.render('Excluir', True, (0,0,0)), (rect_excluir.x+10, rect_excluir.y+5))
                botoes_excluir.append((rect_excluir, serv))
                y += 45
            rect_voltar = pygame.Rect(20, 540, 120, 40)
            pygame.draw.rect(self.screen, (200, 200, 200), rect_voltar)
            label_voltar = self.small_font.render('Voltar', True, (0, 0, 0))
            self.screen.blit(label_voltar, (rect_voltar.x + 20, rect_voltar.y + 7))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.tela_atual = self.menu_principal
                        return
                    if event.key == pygame.K_DOWN:
                        scroll += 45
                    if event.key == pygame.K_UP and scroll > 0:
                        scroll -= 45
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for rect, serv in botoes_editar:
                        if rect.collidepoint(event.pos):
                            self.servico_selecionado = serv
                            self.tela_atual = self.tela_editar_servico
                            return
                    for rect, serv in botoes_excluir:
                        if rect.collidepoint(event.pos):
                            self.servico_selecionado = serv
                            self.tela_atual = self.tela_excluir_servico
                            return
                    if rect_add.collidepoint(event.pos):
                        self.tela_atual = self.tela_adicionar_servico
                        return
                    if rect_voltar.collidepoint(event.pos):
                        self.tela_atual = self.menu_principal
                        return
            self.clock.tick(60)

    def tela_adicionar_servico(self):
        self._tela_form_servico('Adicionar Serviço')

    def tela_editar_servico(self):
        self._tela_form_servico('Editar Serviço', self.servico_selecionado)

    def tela_excluir_servico(self):
        rodando = True
        while rodando:
            self.screen.fill((255, 220, 220))
            msg = self.font.render(f'Excluir serviço?', True, (120,0,0))
            self.screen.blit(msg, (250, 150))
            nome = str(self.servico_selecionado)
            label_nome = self.small_font.render(nome, True, (0,0,0))
            self.screen.blit(label_nome, (250, 200))
            rect_confirma = pygame.Rect(250, 300, 120, 40)
            rect_cancela = pygame.Rect(400, 300, 120, 40)
            pygame.draw.rect(self.screen, (255,180,180), rect_confirma)
            pygame.draw.rect(self.screen, (200,200,200), rect_cancela)
            self.screen.blit(self.small_font.render('Confirmar', True, (0,0,0)), (rect_confirma.x+10, rect_confirma.y+7))
            self.screen.blit(self.small_font.render('Cancelar', True, (0,0,0)), (rect_cancela.x+10, rect_cancela.y+7))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                    
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.tela_atual = self.tela_listar_servicos
                    return
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if rect_confirma.collidepoint(event.pos):
                        servico_controller.excluir_servico(self.servico_selecionado.nome)
                        self.tela_atual = self.tela_listar_servicos
                        return
                    if rect_cancela.collidepoint(event.pos):
                        self.tela_atual = self.tela_listar_servicos
                        return
            self.clock.tick(60)

    def _tela_form_servico(self, titulo, serv=None):
        rodando = True
        nome = serv.nome if serv else ''
        descricao = serv.descricao if serv else ''
        preco = str(serv.preco) if serv else ''
        produtos = produto_controller.listar_produtos()
        produtos_usados = list(serv.produtos_usados) if serv else []
        campo = 0 
        campos = [nome, descricao, preco]
        prod_idx = 0
        qtd_prod = 1
        erro_msg = ''
        pygame.key.start_text_input()
        while rodando:
            self.screen.fill((220, 240, 255))
            t = self.font.render(titulo, True, (0,0,0))
            self.screen.blit(t, (220, 40))
            labels = ['Nome:', 'Descrição:', 'Preço:', 'Produtos usados:']
            for i, label in enumerate(labels):
                cor = (0,0,180) if campo == i else (0,0,0)
                l = self.small_font.render(label, True, cor)
                self.screen.blit(l, (120, 120 + i*60))
                if i < 3:
                    pygame.draw.rect(self.screen, (255,255,255), (300, 115 + i*60, 300, 40))
                    valor = self.small_font.render(campos[i], True, (0,0,0))
                    self.screen.blit(valor, (310, 125 + i*60))
                else:
                    y_prod = 125 + i*60
                    for idx, (prod, qtd) in enumerate(produtos_usados):
                        texto = f"{prod.nome} x{qtd}"
                        label = self.small_font.render(texto, True, (0,0,0))
                        self.screen.blit(label, (310, y_prod + idx*30))

            if campo == 3 and produtos:
                pygame.draw.rect(self.screen, (220, 220, 255), (300, 350, 450, 40))
                prod_selecionado_texto = f"Produto: {produtos[prod_idx].nome} (<-/->) Qtd: {qtd_prod} (Up/Down)"
                self.screen.blit(self.small_font.render(prod_selecionado_texto, True, (0,0,0)), (310, 360))


            rect_add_prod = pygame.Rect(650, 295, 120, 30) 
            pygame.draw.rect(self.screen, (180,255,255), rect_add_prod)
            self.screen.blit(self.small_font.render('Adicionar', True, (0,0,0)), (rect_add_prod.x+10, rect_add_prod.y+5))

            rect_salvar = pygame.Rect(250, 400, 120, 40)
            rect_cancelar = pygame.Rect(400, 400, 120, 40)
            pygame.draw.rect(self.screen, (180,255,180), rect_salvar)
            pygame.draw.rect(self.screen, (200,200,200), rect_cancelar)
            self.screen.blit(self.small_font.render('Salvar', True, (0,0,0)), (rect_salvar.x+20, rect_salvar.y+7))
            self.screen.blit(self.small_font.render('Cancelar', True, (0,0,0)), (rect_cancelar.x+20, rect_cancelar.y+7))
            if erro_msg:
                pygame.draw.rect(self.screen, (255,220,220), (180, 470, 440, 50))
                err_label = self.small_font.render(erro_msg, True, (180,0,0))
                self.screen.blit(err_label, (200, 485))
                ok_rect = pygame.Rect(570, 480, 40, 30)
                pygame.draw.rect(self.screen, (255,180,180), ok_rect)
                self.screen.blit(self.small_font.render('OK', True, (0,0,0)), (ok_rect.x+5, ok_rect.y+5))
            pygame.display.flip()
            for event in pygame.event.get():
                if erro_msg:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if ok_rect.collidepoint(event.pos):
                            erro_msg = ''
                    continue
                if event.type == pygame.QUIT:
                    pygame.key.stop_text_input()
                    return
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.key.stop_text_input()
                        self.tela_atual = self.tela_listar_servicos
                        return
                    if event.key == pygame.K_TAB:
                        campo = (campo + 1) % 4
                    elif event.key == pygame.K_BACKSPACE:
                        if campo < 3 and len(campos[campo]) > 0:
                            campos[campo] = campos[campo][:-1]
                    elif event.key == pygame.K_RETURN:
                        try:
                            if not campos[0]: raise ValueError('Nome obrigatório')
                            if not campos[1]: raise ValueError('Descrição obrigatória')
                            if not campos[2]: raise ValueError('Preço obrigatório')
                            preco_val = float(campos[2])
                            if serv: 
                                dados_para_atualizar = {
                                    "nome": campos[0],
                                    "descricao": campos[1],
                                    "preco": preco_val,
                                    "produtos_usados": produtos_usados
                                }

                                servico_controller.atualizar_servico(serv.nome, **dados_para_atualizar)
                            else: 
                                servico_controller.criar_servico(campos[0], campos[1], preco_val, produtos_usados)
                                
                            pygame.key.stop_text_input()
                            self.tela_atual = self.tela_listar_servicos
                            return
                        except Exception as e:
                            erro_msg = str(e)
                    elif event.unicode and campo < 3 and len(event.unicode) == 1 and not event.key in [pygame.K_TAB, pygame.K_RETURN, pygame.K_ESCAPE, pygame.K_BACKSPACE]:
                        campos[campo] += event.unicode
                    elif campo == 3 and produtos:
                        if event.key == pygame.K_LEFT and prod_idx > 0:
                            prod_idx -= 1
                        if event.key == pygame.K_RIGHT and prod_idx < len(produtos)-1:
                            prod_idx += 1
                        if event.key == pygame.K_UP and qtd_prod < 99:
                            qtd_prod += 1
                        if event.key == pygame.K_DOWN and qtd_prod > 1:
                            qtd_prod -= 1
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if rect_add_prod.collidepoint(event.pos) and produtos:

                        produto_existente = next((p for p, q in produtos_usados if p.nome == produtos[prod_idx].nome), None)
                        if produto_existente:
                            produtos_usados[:] = [(p, q + qtd_prod if p.nome == produto_existente.nome else q) for p, q in produtos_usados]
                        else:
                            produtos_usados.append((produtos[prod_idx], qtd_prod))


                    if rect_salvar.collidepoint(event.pos):
                        try:
                            if not campos[0]: raise ValueError('Nome obrigatório')
                            if not campos[1]: raise ValueError('Descrição obrigatória')
                            if not campos[2]: raise ValueError('Preço obrigatório')
                            preco_val = float(campos[2])
                            if serv:
                                servico_controller.atualizar_servico(serv.nome, nome=campos[0], descricao=campos[1], preco=preco_val, produtos_usados=produtos_usados)
                            else:
                                servico_controller.criar_servico(campos[0], campos[1], preco_val, produtos_usados)
                            pygame.key.stop_text_input()
                            self.tela_atual = self.tela_listar_servicos
                            return
                        except Exception as e:
                            erro_msg = str(e)
                    if rect_cancelar.collidepoint(event.pos):
                        pygame.key.stop_text_input()
                        self.tela_atual = self.tela_listar_servicos
                        return
            self.clock.tick(60)
        pygame.key.stop_text_input()

    def tela_listar_agendamentos(self):
        rodando = True
        scroll = 0
        try:
            ags = agendamento_controller.listar_agendamentos()
        except Exception as e:
            self._mostrar_erro_pygame(f"Erro ao listar agendamentos: {e}")
            ags = []
        while rodando:
            self.screen.fill((245, 245, 245))
            titulo = self.font.render('Agendamentos', True, (0, 0, 0))
            self.screen.blit(titulo, (40, 30))
            rect_add = pygame.Rect(600, 30, 160, 40)
            pygame.draw.rect(self.screen, (180, 255, 180), rect_add)
            self.screen.blit(self.small_font.render('Adicionar', True, (0,0,0)), (rect_add.x+30, rect_add.y+7))
            y = 90 - scroll
            botoes_cancelar = []
            for idx, ag in enumerate(ags, 1):
                pet_nome = getattr(ag.pet, 'nome', '')
                dono_nome = getattr(ag.pet.dono, 'nome', '')
                data_hora = ag.data_horario.strftime('%d/%m/%y %H:%M')
                status = " (Cancelado)" if ag.cancelado else ""
                texto = f"{idx}. {pet_nome} ({dono_nome}) - {data_hora}{status}"
                if len(texto) > 45:
                    texto = texto[:42] + '...'
                label = self.small_font.render(texto, True, (30, 30, 30))
                rect = label.get_rect(topleft=(60, y))
                self.screen.blit(label, rect.topleft)
                if not ag.cancelado:
                    rect_cancelar = pygame.Rect(600, y, 120, 30)
                    pygame.draw.rect(self.screen, (255, 180, 180), rect_cancelar)
                    self.screen.blit(self.small_font.render('Cancelar', True, (0,0,0)), (rect_cancelar.x+10, rect_cancelar.y+5))
                    botoes_cancelar.append((rect_cancelar, ag))
                y += 45
            rect_voltar = pygame.Rect(20, 540, 120, 40)
            pygame.draw.rect(self.screen, (200, 200, 200), rect_voltar)
            label_voltar = self.small_font.render('Voltar', True, (0, 0, 0))
            self.screen.blit(label_voltar, (rect_voltar.x + 20, rect_voltar.y + 7))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.tela_atual = self.menu_principal
                        return
                    if event.key == pygame.K_DOWN:
                        scroll += 45
                    if event.key == pygame.K_UP and scroll > 0:
                        scroll -= 45
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for rect, ag in botoes_cancelar:
                        if rect.collidepoint(event.pos):
                            ag.cancelar()

                    if rect_add.collidepoint(event.pos):
                        self.tela_atual = self.tela_adicionar_agendamento
                        return
                    if rect_voltar.collidepoint(event.pos):
                        self.tela_atual = self.menu_principal
                        return
            self.clock.tick(60)

    def tela_adicionar_agendamento(self):
        self._tela_form_agendamento('Adicionar Agendamento')

    def tela_editar_agendamento(self):
        self.tela_listar_agendamentos()


    def tela_excluir_agendamento(self):
        self.tela_listar_agendamentos()


    def _tela_form_agendamento(self, titulo, ag=None):
        import datetime
        rodando = True
        pets = pet_controller.listar_pets()
        servicos = servico_controller.listar_servicos()
        pet_idx = 0
        servico_idx = 0
        now = datetime.datetime.now() + datetime.timedelta(days=1)
        data = [now.day, now.month, now.year, now.hour, now.minute]
        campo = 0 
        erro_msg = ''
        data_labels = ['Dia', 'Mês', 'Ano', 'Hora', 'Min']
        data_max = [31, 12, 2100, 23, 59]
        data_min = [1, 1, 2023, 0, 0]
        data_idx = 0
        dropdown_pet = False
        dropdown_servico = False
        pygame.key.start_text_input()
        while rodando:
            self.screen.fill((220, 240, 255))
            t = self.font.render(titulo, True, (0,0,0))
            self.screen.blit(t, (220, 40))
            cor = (0,0,180) if campo == 0 else (0,0,0)
            l = self.small_font.render('Pet:', True, cor)
            self.screen.blit(l, (120, 120))
            rect_pet = pygame.Rect(250, 115, 350, 40)
            pygame.draw.rect(self.screen, (255,255,255), rect_pet)
            pet_nome = pets[pet_idx].nome if pets else 'Nenhum pet cadastrado'
            valor = self.small_font.render(pet_nome, True, (0,0,0))
            self.screen.blit(valor, (260, 125))

            dono_nome = pets[pet_idx].dono.nome if pets else ''
            l = self.small_font.render('Dono:', True, (0,0,0))
            self.screen.blit(l, (120, 180))
            pygame.draw.rect(self.screen, (235,235,235), (250, 175, 350, 40))
            valor = self.small_font.render(dono_nome, True, (0,0,0))
            self.screen.blit(valor, (260, 185))

            cor = (0,0,180) if campo == 1 else (0,0,0)
            l = self.small_font.render('Serviço:', True, cor)
            self.screen.blit(l, (120, 240))
            rect_servico = pygame.Rect(250, 235, 350, 40)
            pygame.draw.rect(self.screen, (255,255,255), rect_servico)
            servico_nome = servicos[servico_idx].nome if servicos else 'Nenhum serviço'
            valor = self.small_font.render(servico_nome, True, (0,0,0))
            self.screen.blit(valor, (260, 245))

            cor = (0,0,180) if campo == 2 else (0,0,0)
            l = self.small_font.render('Data:', True, cor)
            self.screen.blit(l, (120, 300))
            rect_data = pygame.Rect(250, 295, 350, 40)
            pygame.draw.rect(self.screen, (255,255,255), rect_data)
            if campo == 2:

                x_base = 260
                for i, txt in enumerate([f"{data[0]:02d}", f"{data[1]:02d}", f"{data[2]}", f"{data[3]:02d}", f"{data[4]:02d}"]):
                    cor_data = (0,0,180) if data_idx == i else (0,0,0)
                    self.screen.blit(self.small_font.render(txt, True, cor_data), (x_base, 305))
                    if i == 0 or i == 1:
                        x_base += 40
                    elif i == 2:
                        x_base += 60
                    else:
                        x_base += 40
                    if i == 0 or i == 1:
                        self.screen.blit(self.small_font.render('/', True, (0,0,0)), (x_base-10, 305))
                    if i == 2:
                        self.screen.blit(self.small_font.render(' ', True, (0,0,0)), (x_base-10, 305))
                    if i == 3:
                        self.screen.blit(self.small_font.render(':', True, (0,0,0)), (x_base-10, 305))
            else:
                data_str = f"{data[0]:02d}/{data[1]:02d}/{data[2]} {data[3]:02d}:{data[4]:02d}"
                valor = self.small_font.render(data_str, True, (0,0,0))
                self.screen.blit(valor, (260, 305))

            if dropdown_pet:
                for i, pet in enumerate(pets):
                    rect_opt = pygame.Rect(250, 155 + i*35, 350, 30)
                    pygame.draw.rect(self.screen, (245,245,255) if i != pet_idx else (200,230,255), rect_opt)
                    label = self.small_font.render(pet.nome, True, (0,0,0))
                    self.screen.blit(label, (260, 160 + i*35))

            if dropdown_servico:
                for i, serv in enumerate(servicos):
                    rect_opt = pygame.Rect(250, 275 + i*35, 350, 30)
                    pygame.draw.rect(self.screen, (245,245,255) if i != servico_idx else (200,230,255), rect_opt)
                    label = self.small_font.render(serv.nome, True, (0,0,0))
                    self.screen.blit(label, (260, 280 + i*35))

            rect_salvar = pygame.Rect(250, 400, 120, 40)
            rect_cancelar = pygame.Rect(400, 400, 120, 40)
            pygame.draw.rect(self.screen, (180,255,180), rect_salvar)
            pygame.draw.rect(self.screen, (200,200,200), rect_cancelar)
            self.screen.blit(self.small_font.render('Salvar', True, (0,0,0)), (rect_salvar.x+20, rect_salvar.y+7))
            self.screen.blit(self.small_font.render('Cancelar', True, (0,0,0)), (rect_cancelar.x+20, rect_cancelar.y+7))
            if erro_msg:
                pygame.draw.rect(self.screen, (255,220,220), (180, 470, 440, 50))
                err_label = self.small_font.render(erro_msg, True, (180,0,0))
                self.screen.blit(err_label, (200, 485))
                ok_rect = pygame.Rect(570, 480, 40, 30)
                pygame.draw.rect(self.screen, (255,180,180), ok_rect)
                self.screen.blit(self.small_font.render('OK', True, (0,0,0)), (ok_rect.x+5, ok_rect.y+5))
            pygame.display.flip()
            for event in pygame.event.get():
                if erro_msg:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if ok_rect.collidepoint(event.pos):
                            erro_msg = ''
                    continue
                if event.type == pygame.QUIT:
                    pygame.key.stop_text_input()
                    return
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.key.stop_text_input()
                        self.tela_atual = self.tela_listar_agendamentos
                        return
                    if event.key == pygame.K_TAB:
                        campo = (campo + 1) % 3
                    elif campo == 2:
                        if event.key == pygame.K_LEFT and data_idx > 0:
                            data_idx -= 1
                        if event.key == pygame.K_RIGHT and data_idx < 4:
                            data_idx += 1
                        if event.key == pygame.K_UP:
                            data[data_idx] = min(data[data_idx]+1, data_max[data_idx])
                        if event.key == pygame.K_DOWN:
                            data[data_idx] = max(data[data_idx]-1, data_min[data_idx])
                    elif event.key == pygame.K_RETURN:
                        try:
                            if not pets: raise ValueError('Selecione um pet')
                            if not servicos: raise ValueError('Selecione um serviço')
                            dt = datetime.datetime(data[2], data[1], data[0], data[3], data[4])
                            if dt <= datetime.datetime.now():
                                raise ValueError('A data deve ser futura')
                            agendamento_controller.criar_agendamento(pets[pet_idx], servicos[servico_idx], dt)
                            pygame.key.stop_text_input()
                            self.tela_atual = self.tela_listar_agendamentos
                            return
                        except Exception as e:
                            erro_msg = str(e)
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if rect_pet.collidepoint(event.pos):
                        dropdown_pet = not dropdown_pet
                        dropdown_servico = False
                    elif rect_servico.collidepoint(event.pos):
                        dropdown_servico = not dropdown_servico
                        dropdown_pet = False
                    elif dropdown_pet:
                        for i, pet in enumerate(pets):
                            rect_opt = pygame.Rect(250, 155 + i*35, 350, 30)
                            if rect_opt.collidepoint(event.pos):
                                pet_idx = i
                                dropdown_pet = False
                                break
                    elif dropdown_servico:
                        for i, serv in enumerate(servicos):
                            rect_opt = pygame.Rect(250, 275 + i*35, 350, 30)
                            if rect_opt.collidepoint(event.pos):
                                servico_idx = i
                                dropdown_servico = False
                                break
                    elif rect_salvar.collidepoint(event.pos):
                        try:
                            if not pets: raise ValueError('Selecione um pet')
                            if not servicos: raise ValueError('Selecione um serviço')
                            dt = datetime.datetime(data[2], data[1], data[0], data[3], data[4])
                            if dt <= datetime.datetime.now():
                                raise ValueError('A data deve ser futura')
                            agendamento_controller.criar_agendamento(pets[pet_idx], servicos[servico_idx], dt)
                            pygame.key.stop_text_input()
                            self.tela_atual = self.tela_listar_agendamentos
                            return
                        except Exception as e:
                            erro_msg = str(e)
                    elif rect_cancelar.collidepoint(event.pos):
                        pygame.key.stop_text_input()
                        self.tela_atual = self.tela_listar_agendamentos
                        return
                    else:
                        dropdown_pet = False
                        dropdown_servico = False
            self.clock.tick(60)
        pygame.key.stop_text_input()

    def tela_listar_vendas(self):
        rodando = True
        scroll = 0
        try:
            vendas = venda_controller.listar_vendas()
        except Exception as e:
            self._mostrar_erro_pygame(f"Erro ao listar vendas: {e}")
            vendas = []
        while rodando:
            self.screen.fill((245, 245, 245))
            titulo = self.font.render('Vendas', True, (0, 0, 0))
            self.screen.blit(titulo, (40, 30))
            rect_add = pygame.Rect(600, 30, 160, 40)
            pygame.draw.rect(self.screen, (180, 255, 180), rect_add)
            self.screen.blit(self.small_font.render('Adicionar', True, (0,0,0)), (rect_add.x+30, rect_add.y+7))
            y = 90 - scroll
            for idx, venda in enumerate(vendas, 1):
                dono_nome = venda.agendamento.pet.dono.nome
                data_hora = venda.agendamento.data_horario.strftime('%d/%m/%y %H:%M')
                valor = venda.valor_total
                texto = f"{idx}. {dono_nome} - {data_hora} - R$ {valor:.2f}"
                if len(texto) > 45:
                    texto = texto[:42] + '...'
                label = self.small_font.render(texto, True, (30, 30, 30))
                rect = label.get_rect(topleft=(60, y))
                self.screen.blit(label, rect.topleft)
                y += 45
            rect_voltar = pygame.Rect(20, 540, 120, 40)
            pygame.draw.rect(self.screen, (200, 200, 200), rect_voltar)
            label_voltar = self.small_font.render('Voltar', True, (0, 0, 0))
            self.screen.blit(label_voltar, (rect_voltar.x + 20, rect_voltar.y + 7))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.tela_atual = self.menu_principal
                        return
                    if event.key == pygame.K_DOWN:
                        scroll += 45
                    if event.key == pygame.K_UP and scroll > 0:
                        scroll -= 45
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if rect_add.collidepoint(event.pos):
                        self.tela_atual = self.tela_adicionar_venda
                        return
                    if rect_voltar.collidepoint(event.pos):
                        self.tela_atual = self.menu_principal
                        return
            self.clock.tick(60)

    def tela_adicionar_venda(self):
        self._tela_form_venda('Adicionar Venda')

    def tela_editar_venda(self):
        self.tela_listar_vendas()

    def tela_excluir_venda(self):
        self.tela_listar_vendas()


    def _tela_form_venda(self, titulo, venda=None):
        rodando = True
        agora = datetime.datetime.now()
        ags = [ag for ag in agendamento_controller.listar_agendamentos() if not ag.cancelado and ag.data_horario > agora]

        ag_idx = 0
        if venda and venda.agendamento in ags:
            ag_idx = ags.index(venda.agendamento)
        
        margem = str(venda.margem_lucro) if venda else '20.0'
        campo = 0 
        erro_msg = ''
        pygame.key.start_text_input()
        while rodando:
            self.screen.fill((220, 240, 255))
            t = self.font.render(titulo, True, (0,0,0))
            self.screen.blit(t, (220, 40))
            labels = ['Agendamento:', 'Produtos do Serviço:', 'Margem de lucro (%):']
            
            l_ag = self.small_font.render(labels[0], True, (0,0,180) if campo == 0 else (0,0,0))
            self.screen.blit(l_ag, (120, 120))
            ag_txt = "Nenhum agendamento disponível"
            if ags:
                ag_selecionado = ags[ag_idx]
                ag_txt = f"{ag_selecionado.pet.nome} - {ag_selecionado.servico.nome} - {ag_selecionado.data_horario.strftime('%d/%m/%Y %H:%M')}"
            pygame.draw.rect(self.screen, (235, 235, 235), (350, 115, 400, 40)) 
            valor = self.small_font.render(ag_txt, True, (0,0,0))
            self.screen.blit(valor, (360, 125))

            l_prod = self.small_font.render(labels[1], True, (0,0,0)) 
            self.screen.blit(l_prod, (120, 180))
            y_prod = 180
            produtos_usados = []
            if ags:
                produtos_usados = list(ags[ag_idx].servico.produtos_usados)
            for idx, (prod, qtd) in enumerate(produtos_usados):
                texto = f"- {prod.nome} x{qtd}"
                label_prod = self.small_font.render(texto, True, (0,0,0))
                self.screen.blit(label_prod, (360, y_prod + idx*30))

            l_margem = self.small_font.render(labels[2], True, (0,0,180) if campo == 1 else (0,0,0))
            self.screen.blit(l_margem, (120, 240))
            pygame.draw.rect(self.screen, (255,255,255), (350, 235, 100, 40)) 
            valor_margem = self.small_font.render(margem, True, (0,0,0))
            self.screen.blit(valor_margem, (360, 245))

            rect_salvar = pygame.Rect(250, 320, 120, 40)
            rect_cancelar = pygame.Rect(400, 320, 120, 40)
            pygame.draw.rect(self.screen, (180,255,180), rect_salvar)
            pygame.draw.rect(self.screen, (200,200,200), rect_cancelar)
            self.screen.blit(self.small_font.render('Salvar', True, (0,0,0)), (rect_salvar.x+20, rect_salvar.y+7))
            self.screen.blit(self.small_font.render('Cancelar', True, (0,0,0)), (rect_cancelar.x+20, rect_cancelar.y+7))
            
            if erro_msg:
                pygame.draw.rect(self.screen, (255,220,220), (180, 400, 440, 50))
                err_label = self.small_font.render(erro_msg, True, (180,0,0))
                self.screen.blit(err_label, (200, 415))
                ok_rect = pygame.Rect(570, 410, 40, 30)
                pygame.draw.rect(self.screen, (255,180,180), ok_rect)
                self.screen.blit(self.small_font.render('OK', True, (0,0,0)), (ok_rect.x+5, ok_rect.y+5))

            pygame.display.flip()
            
            for event in pygame.event.get():
                if erro_msg:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and ok_rect.collidepoint(event.pos):
                        erro_msg = ''
                    continue

                if event.type == pygame.QUIT:
                    pygame.key.stop_text_input()
                    return
                    

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.key.stop_text_input()
                        self.tela_atual = self.tela_listar_vendas
                        return
                    if event.key == pygame.K_TAB:
                        campo = (campo + 1) % 2
                    
                    if campo == 0 and ags: 
                        if event.key == pygame.K_UP and ag_idx > 0:
                            ag_idx -= 1
                        if event.key == pygame.K_DOWN and ag_idx < len(ags)-1:
                            ag_idx += 1
                    
                    elif campo == 1: 
                        if event.key == pygame.K_BACKSPACE:
                            margem = margem[:-1]
                        elif event.unicode.isdigit() or event.unicode == '.':
                            margem += event.unicode

                    if event.key == pygame.K_RETURN:
                        try:
                            if not ags: raise ValueError('Nenhum agendamento para venda')
                            produtos_usados = list(ags[ag_idx].servico.produtos_usados)
                            margem_val = float(margem)
                            venda_controller.criar_venda(ags[ag_idx], produtos_usados, [], margem_val)
                            pygame.key.stop_text_input()
                            self.tela_atual = self.tela_listar_vendas
                            return
                        except Exception as e:
                            erro_msg = str(e)
                
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if rect_salvar.collidepoint(event.pos):
                        try:
                            if not ags: raise ValueError('Nenhum agendamento para venda')
                            produtos_usados = list(ags[ag_idx].servico.produtos_usados)
                            margem_val = float(margem)
                            venda_controller.criar_venda(ags[ag_idx], produtos_usados, [], margem_val)
                            pygame.key.stop_text_input()
                            self.tela_atual = self.tela_listar_vendas
                            return
                        except Exception as e:
                            erro_msg = str(e)
                    if rect_cancelar.collidepoint(event.pos):
                        pygame.key.stop_text_input()
                        self.tela_atual = self.tela_listar_vendas
                        return
            self.clock.tick(60)
        pygame.key.stop_text_input()

    def tela_relatorio_geral_vendas(self):
        vendas = venda_controller.listar_vendas()
        if not vendas:
            self._mostrar_erro_pygame("Nenhuma venda registrada.")
            self.tela_atual = self.menu_relatorios
            return

        relatorio = relatorio_controller.gerar_relatorio_vendas(vendas)
        linhas = [
            f"Total de Vendas: R$ {relatorio.get('total_vendas', 0):.2f}",
            f"Quantidade de Vendas: {relatorio.get('quantidade_vendas', 0)}",
            f"Média por Venda: R$ {relatorio.get('media_vendas', 0):.2f}",
            f"Maior Venda: R$ {relatorio.get('maior_venda', 0):.2f}",
            f"Menor Venda: R$ {relatorio.get('menor_venda', 0):.2f}",
        ]
        self._tela_listagem('Relatório Geral de Vendas', linhas, self.menu_relatorios)
    
    def tela_relatorio_donos_por_gasto(self):
        vendas = venda_controller.listar_vendas()
        if not vendas:
            self._mostrar_erro_pygame("Nenhuma venda registrada.")
            self.tela_atual = self.menu_relatorios
            return
        
        ranking = relatorio_controller.gerar_ranking_donos_por_gasto(vendas)
        linhas = [f"{dono.nome}: R$ {gasto:.2f}" for dono, gasto in ranking]
        self._tela_listagem('Ranking de Donos por Gasto', linhas, self.menu_relatorios)

    def tela_relatorio_pets_por_vendas(self):
        vendas = venda_controller.listar_vendas()
        if not vendas:
            self._mostrar_erro_pygame("Nenhuma venda registrada.")
            self.tela_atual = self.menu_relatorios
            return

        ranking = relatorio_controller.gerar_ranking_pets_por_vendas(vendas)
        linhas = [f"{pet.nome} ({pet.dono.nome}): {num_vendas} vendas" for pet, num_vendas in ranking]
        self._tela_listagem('Ranking de Pets por Vendas', linhas, self.menu_relatorios)

    def tela_relatorio_produtos_mais_usados(self):
        vendas = venda_controller.listar_vendas()
        if not vendas:
            self._mostrar_erro_pygame("Nenhuma venda registrada.")
            self.tela_atual = self.menu_relatorios
            return

        ranking = relatorio_controller.gerar_relatorio_produtos_mais_usados(vendas)
        linhas = [f"{produto.nome}: {quantidade} unidades" for produto, quantidade in ranking]
        self._tela_listagem('Produtos Mais Usados', linhas, self.menu_relatorios)

    def tela_relatorio_servicos_mais_vendidos(self):
        vendas = venda_controller.listar_vendas()
        if not vendas:
            self._mostrar_erro_pygame("Nenhuma venda registrada.")
            self.tela_atual = self.menu_relatorios
            return
        
        ranking = relatorio_controller.gerar_relatorio_servicos_mais_vendidos(vendas)
        linhas = [f"{servico.nome}: {num_vendas} vezes" for servico, num_vendas in ranking]
        self._tela_listagem('Serviços Mais Vendidos', linhas, self.menu_relatorios)


    def _tela_listagem(self, titulo_str, linhas, tela_retorno):
        rodando = True
        scroll = 0
        while rodando:
            self.screen.fill((245, 245, 245))
            titulo = self.font.render(titulo_str, True, (0, 0, 0))
            self.screen.blit(titulo, (60, 30))
            y = 90 - scroll
            for idx, linha in enumerate(linhas, 1):
                texto = f"{idx}. {linha}"
                label = self.small_font.render(texto, True, (30, 30, 30))
                self.screen.blit(label, (60, y))
                y += 35

            rect_voltar = pygame.Rect(20, 540, 120, 40)
            pygame.draw.rect(self.screen, (200, 200, 200), rect_voltar)
            label_voltar = self.small_font.render('Voltar', True, (0, 0, 0))
            self.screen.blit(label_voltar, (rect_voltar.x + 20, rect_voltar.y + 7))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.tela_atual = tela_retorno
                        return
                    if event.key == pygame.K_DOWN:
                        scroll += 35
                    if event.key == pygame.K_UP and scroll > 0:
                        scroll -= 35
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if rect_voltar.collidepoint(event.pos):
                        self.tela_atual = tela_retorno
                        return
            self.clock.tick(60)

    def tela_stub(self, nome):
        rodando = True
        while rodando:
            self.screen.fill((245, 245, 245))
            titulo = self.font.render(f'{nome.capitalize()}', True, (0, 0, 0))
            self.screen.blit(titulo, (250, 100))
            instrucao = self.small_font.render('Pressione ESC ou clique em Voltar', True, (100, 100, 100))
            self.screen.blit(instrucao, (170, 200))
            rect_voltar = pygame.Rect(20, 540, 120, 40)
            pygame.draw.rect(self.screen, (200, 200, 200), rect_voltar)
            label_voltar = self.small_font.render('Voltar', True, (0, 0, 0))
            self.screen.blit(label_voltar, (rect_voltar.x + 20, rect_voltar.y + 7))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                    
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.tela_atual = self.menu_principal
                    return
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if rect_voltar.collidepoint(event.pos):
                        self.tela_atual = self.menu_principal
                        return
            self.clock.tick(60)