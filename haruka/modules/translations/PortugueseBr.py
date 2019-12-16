RUN_STRINGS = (
    "Para onde você pensa que está indo?",
    "Hein? o que? Foram embora?",
    "ZZzzZZzz... Eh? O que? Ohh, novamente, isso não importa.",
    "Volte aqui!",
    "Não tão rápido...",
    "Cuidado com a parede!",
    "Não me deixe sozinho com eles!",
    "Se você correr, você morre.",
    "Você me fode, eu estou em todo lugar",
    "Você vai se arrepender disso ...",
    "Você também pode tentar /kickme, acho divertido.",
    "Vá reclamar em outro lugar, ninguém se importa aqui.",
    "Você pode correr, mas não pode se esconder.",
    "É tudo o que você tem?",
    "Estou atras de você...",
    "Você tem companhia!",
    "Podemos fazer isso por bem ou mal.",
    "Você não entendeu, certo?",
    "Se isso, melhor correr.",
    "Se correr o bicho pega se ficar o bicho come.",
    "Eu correria mais rápido se fosse você.",
    "Esse é definitivamente o androide que estamos procurando.",
    "Que a sorte esteja do seu lado.",
    "Famosas últimas palavras.",
    "E eles desapareceram para sempre, para nunca mais serem vistos.",
    "\"Oh olha! Como sou legal, posso escapar de um bot!\" - essa pessoa",
    "Sim, sim, escreva /kickme para ver.",
    "Pegue, pegue este anel e converse com Mordor enquanto estiver com ele.",
    "As lendas têm, eles ainda estão trabalhando...",
    "Ao contrário de Harry Potter, seus pais não podem se proteger de mim.",
    "O medo leva à raiva. A raiva leva ao ódio. O ódio leva ao sofrimento. Se você continuar correndo com medo, poderá "
    "Seja o próximo Vader.",
    "Após muitos cálculos, concluí que meu interesse pelas suas merdas é 0.",
    "Lendas são contadas, elas ainda funcionam.",
    "Continue assim, não tenho certeza se queremos você aqui de qualquer maneira.",
    "Você é um mag- Oh. Espera Você não é o Harry, continue.",
    "NÃO FUNCIONA NOS CORREDORES",
    "Hasta la vista, baby.",
    "Quem deixou os cães saírem?",
    "É engraçado porque ninguém se importa.",
    "Ah, que desperdício. Eu gostei desse.",
    "Francamente, querida, eu não dou a mínima.",
    "Meu milk-shake traz todas as crianças para o parquinho... Então corra mais rápido!",
    "Você não suporta a verdade!",
    "Há muito tempo, em uma galáxia distante... Alguém teria se importado com isso. Embora não seja mais.",
    "Ei, olhe para eles! Eles estão escapando do ban inevitável... Que animais.",
    "Han atira primeiro. Eu também.",
    "Do que você está fugindo, de um coelho branco?",
    "Como diria o Doutor... Corre!",
)

SLAP_TEMPLATES = (
    "{user1} {hits} {user2} com {item}.",
    "{user1} {hits} {user2} na cara com {item}.",
    "{user1} {hits} {user2} no peito com {item}.",
    "{user1} {throws} {item} no {user2}.",
    "{user1} {throws} {item} na cara do {user2} .",
    "{user1} joga {item} na cabeça do {user2}.",
    "{user1} pensa em bater no {user2} com {item}.",
    "{user1} derruba {user2} e repetidamente o {hits} com {item}.",
    "{user1} pega {item} e {hits} no {user2}.",
    "{user1} amarra {user2} em uma cadeira e {throws} {item}.",
    "{user1} deu um empurrão amigável no {user2} para que ele aprenda a nadar na lava"
)

ITEMS = (
    "uma panela de metal",
    "uma truta",
    "um taco de beisebol",
    "um taco de críquete",
    "uma bengala de madeira",
    "uma unha",
    "um Nokia 3310",
    "uma impressora",
    "um projetor",
    "um livro de física",
    "uma torradeira",
    "um Play Station 2 Fat",
    "uma televisão",
    "um caminhão de 5 toneladas",
    "um tubo cheio de fezes",
    "um livro",
    "um Xbox",
    "uma tartaruga morta",
    "um saco de pedras",
    "uma cueca usada",
    "uma galinha de borracha",
    "um vibrador gigante",
    "un extintor",
    "um pedaço de merda petrificada",
    "um liquidificador",
    "um papel queimado",
    "um pedaço de carne",
    "um osso",
    "uma vaca",
)

THROW = (
    "joga",
    "arremessa",
    "mandris",
    "arremessa",
)

HIT = (
    "golpeia",
    "bate",
    "golpeia",
    "esmurra",
    "ataca",
)

MARKDOWN_HELP = """
Você pode usar o markdown para tornar suas mensagens mais expressivas. Este é o markdown atualmente suportado:

<code>palavras de código</code> os acentos graves permitem agrupar suas palavras em fontes monoespaçadas. Mostra como: <code>palavras de código</code>
<code>*palavras em negrito*</code> asteriscos são usadas para fontes em negrito. Mostra como: <b>palavras em negrito</b>
<code>_palavras em itálico_</code> sublinhados são usados ​​para itálico. Mostra como: <i>palavras em itálico</i>
<code>[hyperlink](example.com)</code> isso é usado para <code>[hyperlink](example.com)</code>, and will show as such: hyperlink. Certifique-se de não adicionar espaços extras entre o ] e o ( ou não será um markdown válido.

Agora, se você quiser ter botões em sua mensagem, poderá usar esta sintaxe especial:
<code>[botão](buttonurl://example.com)</code>
Isso criará um botão chamado "botão" que redireciona o usuário para example.com ao clicar.
Se você deseja adicionar dois botões na mesma linha, adicione: same no final do seu link; colocará na mesma linha que a outra. Por exemplo:
<code>[botão](buttonurl://example.com)
[botão2](buttonurl://example.com:same)
[botão 3](buttonurl://example.com)</code>
criará dois botões na mesma linha (botões 1 e 2) e um último (botão 3) em uma segunda linha.

Recheios:
Você também pode usar determinadas tags para preencher sua mensagem com informações de usuário ou bate-papo;  as opções são:
<code>{first}</code>: O primeiro nome do usuário.
<code>{last}</code>: O sobrenome do usuário.
<code>{fullname}</code>: O nome completo do usuário.
<code>{username}</code>: O nome de usuário do usuário; se nenhum estiver disponível, menciona o usuário.
<code>{mention}</code>: Menciona o usuário, usando seu primeiro nome.
<code>{id}</code>: O ID do usuário.
<code>{chatname}</code>: O nome do bate-papo.
<code>{rules}</code>: Adiciona um link para as regras do grupo.
<code>{preview}</code>: Ativa as visualizações de links para a mensagem. Pode ser útil ao usar links para páginas do Instant View.

Um exemplo de como usar recheios seria definir suas boas-vindas, via:
<code>/setwelcome Olá {first}! Bem-vindo à {chatname}.</code>

Experimente isto em notas, filtros, mensagens de boas-vindas ou até regras!
"""

PortugueseBrStrings = {

#Connections
    "Disabled connections to this chat for users": "Conexões desativadas para usuários neste grupo",
    "Enabled connections to this chat for users": "Conexões ativadas para usuários neste grupo",
    "Please enter on/yes/off/no in group!": "Por favor, escreva on/yes/off/no no grupo!",
    "Successfully connected to *{}*": "Conectado com sucesso a *{}*",
    "Connection failed!": "Falha na conexão!",
    "Connections to this chat not allowed!": "Conexões não permitidas neste grupo!",
    "Write chat ID to connect!": "Digite o ID do grupo para se conectar!",
    "Usage limited to PMs only!": "Use restrito apenas a mensagens privadas",

#Misc
    "RUNS-K": RUN_STRINGS,
    "SLAP_TEMPLATES-K": SLAP_TEMPLATES,
    "ITEMS-K": ITEMS,
    "HIT-K": HIT,
    "THROW-K": THROW,
    "ITEMP-K": ITEMS,
    "ITEMR-K": ITEMS,
    "MARKDOWN_HELP-K": MARKDOWN_HELP,

    "The original sender, {}, has an ID of `{}`.\nThe forwarder, {}, has an ID of `{}`.":
        "O remetente, {}, tem o ID `{}`.\nO receptor, {}, tem o ID `{}`.",
    "{}'s id is `{}`.": "{} ID - `{}`.",
    "Your id is `{}`.": "Seu ID - `{}`.",
    "This group's id is `{}`.": "ID deste grupo - `{}`.",

    "I can't extract a user from this.": "Não consigo extrair o ID deste usuário",
    "<b>User info</b>:": "<b>Informações do usuário</b>:",
    "\nFirst Name: {}": "\nNome: {}",
    "\nLast Name: {}": "\nSobrenome: {}",
    "\nUsername: @{}": "\nNome de usuário: @{}",
    "\nUser link: {}\n": "\nLink do usuário: {}",
    "\n\nThis person is my owner - I would never do anything against them!":
        "\n\nEssa pessoa é meu dono, eu nunca faria algo contra ela!",
    "\nThis person is one of my sudo users! Nearly as powerful as my owner - so watch it.":
        "\nEssa pessoa é um dos meus usuários Sudo! Tem quase tanto poder quanto meu dono, então tenha cuidado",
    "\nThis person is one of my support users! Not quite a sudo user, but can still gban you off the map.":
        "\nEssa pessoa é um dos meus usuários suporte. Não é como um usuário sudo, mas pode te banir globalmente, tenha cuidado!",
    "\nThis person has been whitelisted! That means I'm not allowed to ban/kick them.":
        "\nEssa pessoa está na lista branca. Isso significa que eu não posso banir ou removê-la.",

    "Its always banhammer time for me!": "É sempre a hora do martelo do ban para mim!",

    "It's {} in {}": "Está {} em {}",
    
    "\nAll commands can either be used with `/` or `!`.\n": "\nTodos os comandos podem ser usados ​​com `/` ou `!`.\n",
    
    "Yes.": "Sim.",
    "No.": "Não.",
    "Maybe.": "Talvez.",
    
    "Sticker kanged successfully! \nPack can be found [here](t.me/addstickers/{packname})": "Sticker kangado com sucesso! \nPacote pode ser achado [aqui](t.me/addstickers/{packname})",
    
    "Please reply to a sticker to get its ID.": "Por favor responda a um stickerer para obeter o seu ID.",
    "Please reply to a sticker for me to upload its PNG.": "Por favor, responda a um sticker para que eu possa upar seu PNG .",

    "Write a location to check the weather.": "Escreva um local para ver como está o tempo.",
    "I will keep an eye on both happy and sad times!": "Estarei aqui nos bons e maus momentos!",
    "Today in {} is being {}, around {}°C.\n": "Hoje em {} está fazendo {}, por volta de {}°C.\n",
    "Sorry, location not found.": "Desculpe, local não encontrado.",

    "Deleting identifiable data...": "Excluindo dados do usuário...",

    "Try forwarding the following message to me, and you'll see!":
        "Tente me enviar a seguinte mensagem e você verá!",
    "/save test This is a markdown test. _italics_, *bold*, `code`, [URL](example.com) [button](buttonurl:github.com) [button2](buttonurl://google.com:same)":
    """/save teste Este é um teste de markdown _itálico_, *negrito*, `código`, \
[URL](example.com) 
[Botão](buttonurl:github.com)
[Botão2](buttonurl://google.com:same)""",

#Misc GDPR
"send-gdpr": """Suas informações pessoais foram excluídas.\n\nLembre-se de que isso não vai remover você \
de qualquer bate-papo, já que são dados do Telegram, NÃO dados do Hitsuki Bot.
Flooding, avisos e proibições globais também são preservados, desde \
[isto](https://ico.org.uk/for-organisations/guide-to-the-general-data-protection-regulation-gdpr/individual-rights/right-to-erasure/), "
que afirma claramente que o direito de cancelamento não se aplica \
\"para a realização de uma tarefa realizada no interesse público.\", assim como \
o caso dos dados mencionados acima.""",

#Admin
"How am I meant to promote someone who's already an admin?": "Como vou promover alguém que já é um administrador?",
"I can't promote myself! Get an admin to do it for me.": "Eu não posso me tornar um administrador! Notifique um administrador para fazer isso!",
"Successfully promoted in *{}*!": "Promovido com sucesso em *{}*!",
"I can't promote/demote people here! Make sure I'm an admin and can appoint new admins.": "Não posso promover/rebaixar pessoas aqui! Certifique-se de que sou administrador e de que posso nomear novos administradores.",

"This person is the CREATOR of the chat, how would I demote them?": "Essa pessoa é o CRIADOR do grupo, como eu a rebaixaria?",

"Can't demote those who weren't promoted!": "Não é possível rebaixar aqueles que não foram promovidos!",

"Successfully demoted in *{}*!": "Rebaixado com sucesso em *{}*!",
"Could not demote. I might not be admin, or the admin status was appointed by another user, so I can't act upon them!": "Não consigo remover o administrador. Pode ser que ele não seja um administrador ou o status de administrador foi atribuído por outro usuário, por isso não posso agir de acordo!",

"I don't have access to the invite link, try changing my permissions!": "Não tenho acesso ao link do convite, tente alterar as minhas permissões!",
"I can only give you invite links for supergroups and channels, sorry!": "Desculpe, só posso dar links de convite para supergrupos e canais.",

"Admins in": "Administradores em",
"this chat": "este chat",
" (Creator)": " (Criador)",

#AFK
"{fst_name} is AFK!": "{} está AFK!",
"firstname} is no longer AFK!": "{} Não está mais AFK!",
"{fst_name} is AFK!": "{} está AFK!",
"{fst_name} is AFK! says its because of:\n{user.reason}": "{} está AFK! Disse que é por causa: \n{}",

#Antiflood
"I like to leave the flooding to natural disasters. But you, you were just a disappointment. Get out.":
     "Suelo tener bastante paciencia con la gente pesada, pero te has pasado. ¡Largo de aquí!",
"I can't kick people here, give me permissions first! Until then, I'll disable antiflood.":
    "No puedo expulsar a la gente aquí, dame permisos primero! Hasta que eso ocurra deshabilitaré el antiflood.",
"Antiflood has been disabled.": "Antiflood ha sido deshabilitado.",
"Antiflood has to be either 0 (disabled), or a number bigger than 3 (enabled)!":
    "Antiflood tiene que ser 0 (deshabilitado), o un número superior a 3 (habilitado)!",
"Antiflood has been updated and set to {}": "Antiflood se ha actualizado y ha sido establecido a {}",
"Unrecognised argument - please use a number, 'off', or 'no'.":
    "Comando desconocido- por favor usa un número, 'off', o 'no'.",
"I'm not currently enforcing flood control!": "Ahora mismo no estoy no controlando el flood!",
"I'm currently banning users if they send more than {} consecutive messages.":
     "Estoy baneando a todos los usuarios que envíen más de {} mensajes consecutivos.",

#Antispam
"I've enabled antispam security in this group. This will help protect you from spammers, unsavoury characters, and the biggest trolls.":
 "He activado la seguridad antispam en este grupo. Esto te ayudará a protegerte contra spammers, personas desagradables y trolls.",

"I've disabled antispam security in this group. GBans wont affect your users anymore. You'll be less protected from any trolls and spammers though!":
    "He desactivado la seguridad antispam en este grupo. Los Bans Globales no afectarán a los usuarios. Estarás menos protegido de trolls y spammers!",

"Give me some arguments to choose a setting! on/off, yes/no!\n\nYour current setting is: {}\nWhen True, any gbans that happen will also happen in your group. When False, they won't, leaving you at the possible mercy of spammers.":
    "Dame algún comando para establecer la configuración! on/off, yes/no!\n\nTu configuración actual es: {}\nCuando sea True, cualquier Ban Global que ocurra tambien ocurrirá en tu grupo. Cuando sea False, los Ban Globales no afectarán en tu grupo, dejandolo a merced de posibles spammers.",

"Globally banned: <b>{}</b>": "Banido globalmente: <b>{}</b>",
"\nGlobally muted: <b>{}</b>": "\nSilenciado globalmente: <b>{}</b>",
"\nReason: {}": "\nMotivo: {}",

#Bans
    "I really wish I could ban admins...": "eu gostaria de poder banir administradores porem...",
    "I'm not gonna BAN myself, are you crazy?": "Não vou banir eu mesmo, está ficando loco?",
    "Banned!": "Banido!",
    "Well damn, I can't ban that user.": "Merda, não consigo banir este usuário!.",
    "You haven't specified a time to ban this user for!": 
        "No foi especificado o tempo para deixar este usuários banido este usuario!",
    "Banned! User will be banned for {}.": "Banido! O usuario foi banido por {}.",

#Blacklist
    "<b>Current blacklisted words in {}:</b>\n": "<b>Palavras na lista negra em {}:</b>\n",
    "There are no blacklisted messages in <b>{}</b>!": "Não há mensagens na lista negra em <b>{}</b>!",
    "Added <code>{}</code> to the blacklist in <b>{}</b>!":
        "Adicionado <code>{}</code> na lista negra de <b>{}</b>!",
    "Tell me which words you would like to add to the blacklist.":
        "Diga-me que palavras você gostaria de adicionar à lista negra.",
    "Removed <code>{}</code> from the blacklist in <b>{}</b>!":
        "Removido <code>{}</code> da lista negra em <b>{}</b>!",
    "This isn't a blacklisted trigger...!": "Este não é um comando da lista negra...!",
    "None of these triggers exist, so they weren't removed.":
        "Nenhum desses comandos existia, portanto eles não foram excluídos.",
    "Removed <code>{}</code> triggers from the blacklist in <b>{}</b>! {} did not exist, so were not removed.":
        "Removido <code>{}</code> dos comandos da lista negra em <b>{}</b>! {} no existe, así que no ha sido borrado!.",
    "Tell me which words you would like to remove from the blacklist.":
        "Diga-me que palavras você gostaria de remover da lista negra.",

    #Filters
    "*Filters in {}:*\n": "*Lista de filtros em {}:*\n",
    "local filters": "filtros locais",
    "*local filters:*\n": "*filtros locais:*\n",
    "No filters in {}!": "Nenhum filtro em {}!",
    "There is no note message - You can't JUST have buttons, you need a message to go with it!":
        "Não há mensagem de nota - Você NÃO pode APENAS ter botões, precisa de uma mensagem para acompanhar!",
    "You didn't specify what to reply with!": "Você não especificou o que deseja que eu responda!",
    "Handler '{}' added in *{}*!": "O filtro '{}' foi adicionado em *{}*!",
    "No filters are active in {}!": "Nenhum filtro ativo em {}!",
    "Yep, I'll stop replying to that in *{}*." : "Sim, vou parar de responder a isso em *{}*.",
    "That's not a current filter - run /filters for all active filters.":
        "Esse filtro não existe - escreva /filters para ver os filtros ativos.",
    
    #Disable
    "Disabled the use of `{}` in *{}*": "Desativado o uso de `{}` em *{}*",
    "That command can't be disabled": "Esse comando não pode ser desativado!",
    "What should I disable?": "O que devo desativar?",

    "Enabled the use of `{}` in *{}*": "Ativado o uso de `{}` em *{}*",
    "Is that even disabled?": "Isso está desativado?",
    "What should I enable?": "O que devo ativar?",

    "The following commands are toggleable:\n{}": "Os seguintes comando podem ser desativados:\n{}",
    "No commands can be disabled.": "Não há comandos que possam ser desativados.",
    "No commands are disabled in *{}*!": "Não há comandos desabilitados em *{}*!",
    "No commands are disabled!": "Não há comandos desativados!",
    "The following commands are currently restricted in *{}*:\n{}":
        "Os seguintes comandos estão desativados em *{}*:\n{}",

#Locks
    "Locked {} messages for all non-admins!": "Bloqueados los mensajes de {}  para todos los no administradores!",
    "What are you trying to lock...? Try /locktypes for the list of lockables":
        "¿Qué estás intentando bloquear...? Escribe /locktypes para ver la lista de los tipos de bloqueos.",
    "I'm not an administrator, or haven't got delete rights.":
        "No soy administrador o no tengo permisos para borrar.",
    "Unlocked {} for everyone!": "Desbloqueado {} para todos!",
    "What are you trying to unlock...? Try /locktypes for the list of lockables":
        "¿Qué estás intentando desbloquear...? Escribe /locktypes para ver la lista de los tipos de bloqueos.",
    "What are you trying to unlock...?": "¿Qué estás intentando desbloquear...?",
    "I see a bot, and I've been told to stop them joining... but I'm not admin!":
        "He visto un bot y se me ha ordenado evitar que entre al grupo..., pero no soy administrador!",
    "Only admins are allowed to add bots to this chat! Get outta here.":
        "¡Solo se permite a los administradores añadir bots! ¡Fuera de aquí!",
    "There are no current locks in *{}*.": "No hay bloqueos en *{}*.",
    "These are the locks in *{}*:": "Estos son los bloqueos en *{}*:",
    "this chat": "este chat",

#Log channel
    "Now, forward the /setlog to the group you want to tie this channel to!":
        "Ahora envia /setlog al grupo con el que quieres vincular este canal!",
    "This channel has been set as the log channel for {}.": 
        "Este canal ha sido configurado como el canal de registro para {}.",
    "Successfully set log channel!": "Canal de registro establecido con éxito!",
    "*The steps to set a log channel are:*\n • add bot to the desired channel\n • send /setlog to the channel\n • forward the /setlog to the group\n":
        """*Los pasos para establecer un canal de registro son:*
 • añade el bot al canal que quieras!)
 • escribe /setlog en el canal
 • envía el /setlog que has puesto en el canal al grupo.""",

    "Channel has been unlinked from {}": "El canal ha sido desvinculado de {}",
    "Log channel has been un-set.": "Canal de registro no establecido.",
    "No log channel has been set yet!": "No hay ningún canal de registro establecido!",

#Users
    "I've seen them in <code>{}</code> chats in total.": 
        "Eu vi ele em <code>{}</code> grupos no total.",
    "I've seen them in... Wow. Are they stalking me? They're in all the same places I am... oh. It's me.":
        "Eu o vi em... Uau.  Você está me seguindo você está nos mesmos lugares que eu... Oh, mas sou eu!",
    
#Msg_deleting
    "Cannot delete all messages. The messages may be too old, I might not have delete rights, or this might not be a supergroup.":
        "Não foi possível apagar todas as mensagens. As mensagens podem ser muito antigas, ou não tenho direitos para excluí-las ou este grupo pode não ser um supergrupo.",
    "Purge complete.": "Limpeza concluída.",
    "Reply to a message to select where to start purging from.":
        "Responda a uma mensagem para selecionar de onde iniciar a limpeza.",
    "Whadya want to delete?": "O que você deseja apagar?",

#Muting
    "You'll need to either give me a username to mute, or reply to someone to be muted.":
        "Necesitas darme un nombre de usuario para silenciar, o responde a alguien para silenciarle.",
    "I'm not muting myself!": "¡No me voy a silenciar a mi misma!",
    "Afraid I can't stop an admin from talking!": "¡Me temo que no puedo hacer que un administrador pare de hablar!",
    "You'll need to either give me a username to unmute, or reply to someone to be unmuted.":
        "Necesitas darme un nombre de usuario para dejar de silenciarle, o responde a alguien que está silenciado para quitarle el silencio.",
    "This user already has the right to speak in {}.": "Este usuario ya puede hablar en {}.",
    "Yep, {} can start talking again in {}!": "Si, {} puede empezar a hablar otra vez en {}!",
    "This user isn't even in the chat, unmuting them won't make them talk more than they already do!":
        "Este usuario ni siquiera está en el chat.",
    "I really wish I could mute admins...": "Ya me gustaría poder silenciar a administradores...",
    "I'm not gonna MUTE myself, are you crazy?" : "No voy a silenciarme a mi misma, ¿estás loco?",
    "You haven't specified a time to mute this user for!":
        "¡No has especificado el tiempo para silenciar a este usuario!",
    "Muted for {} in {}!": "Silenciado durante {} en {}!",
    "This user is already muted in {}!": "Este usuario ya está silenciado.",
    "Well damn, I can't mute that user.": "Vaya, no puedo silenciar a este usuario.",

    "You'll need to either give me a username to restrict, or reply to someone to be restricted.":
        "Necesitas darme un nombre de usuario para restringir, o responder a alguien para restringirle.",
    "I'm not restricting myself!": "No me voy a restringir a mi misma!",
    "Afraid I can't restrict admins!": "Me temo que no puedo restringir a administradores!",
    "{} is restricted from sending media in {}!": "{} ha sido restringido para enviar media en {}!",
    "This user is already restricted in {}!": "Este usuario ya está restringifo en {}!",
    "This user isn't in the {}!": "Este usuario no está en {}!",

    "You'll need to either give me a username to unrestrict, or reply to someone to be unrestricted.":
        "Necesitas darme un nombre de usuario para quitar la restricción, o responder a un mensaje de esa persona.",
    "This user already has the rights to send anything in {}.": 
        "Este usuario ya tiene permisos para enviar cualquier cosa en {}.",
    "Yep, {} can send media again in {}!": "Si, {} puede volver a enviar media en {}!",
    "This user isn't even in the chat, unrestricting them won't make them send anything than they already do!":
        "ЭEste usuario ni siquiera está en el chat.",
    "I really wish I could restrict admins...": "Ya me gustaría poder restringir a administradores...",
    "I'm not gonna RESTRICT myself, are you crazy?": "No voy a restringirme a mi misma, ¿estás loco?",
    "You haven't specified a time to restrict this user for!": 
        "¡No has especificado el tiempo para restringir a este usuario!",
    "Well damn, I can't restrict that user.": "Vaya, no puedo restringir a este usuario.",
    "{} is muted in {}!": "{} está silenciado en {}!",
    "Restricted from sending media for {} in {}!": "Restringido para enviar mídia por {} em {}!",
    "Restricted for {} in {}!": "{} Restringido por {} em {}!",

#Notes
    "Get rekt": "Te despedaçou!",


#Multi
    "Invalid Chat ID provided!": "O ID deste grupo não é válido", #Connections
    "You don't seem to be referring to a user.": "Parece que você não está se referindo à um usuário.", #Admin, Bans, Muting
    "I can't seem to find this user": "Eu não consigo encontrar este usuário.", #Bans, Muting
    "Yes": "Sim", #Antispam
    "No": "Não", #Antispam

#__main__
    #Module names
        "Admin": "Administrador",
        "AFK": "Ausente (AFK)",
        "AntiFlood": "Anti-Flood",
        "Bans": "Banimentos",
        "Word Blacklists": "Lista negra",
        "Filters": "Filtros",
        "Command disabling": "Desativar comandos",
        "Antispam security": "Segurança Anti-Spam",
        "Locks": "Bloqueios",
        "Log Channels": "Canais de registro",
        "Misc": "Diversos",
        "Purges": "Limpeza",
        "Notes": "Notas",
        "Reporting": "Reportar",
        "Rules": "Regras",
        "Connections": "Conexões",
        "Warnings": "Advertências",
        "Greetings": "Saudações",
        "Image Lookup": "Pesquisa de imagens",
        "Direct Links": "Links diretos",
        "Dogs and Cats": "Cachorros e Gatos",
        "Translator": "Tradutor",
        "Domain Blacklists": "Lista negra de domínios",
        "Federation": "Federações",
        "Stickers": "Adesivos",
        "Memes and etc.": "Memes e etc.",
        "Reactions": "Reações",
        "Sed/Regex": "Sed/Regex",

#Some main stuff
"Here is the help for the *{}* module:\n{}": "Aqui está a ajuda para o módulo *{}*:\n{}",
"Back": "Voltar",

    "send-help": """Olá! Meu nome é *{}*.
Eu sou um bot para administração de grupos modular com alguns extras divertidos! Confira o seguinte para ter uma idéia de algumas das coisas em que posso ajudá-lo.

Principais comandos:
 - /start: inicia o bot
 - /help: te envia uma mensagem privada com as informações.
 - /help <module name>: te envia uma mensagem privada com as informações deste comando.
 - /lang: altera o idioma do bot
 - /settings:
   - em um grupo: o redirecionará para o PV, com todas as configurações do determinado grupo.
   {}
   """,

    "send-group-settings": """Oi! Existem algumas configurações disponíveis para *{}* - entre e selecione o que
você tiver interesse""",

#Misc
"RUNS-K": RUN_STRINGS,
"SLAP_TEMPLATES-K": SLAP_TEMPLATES,
"ITEMS-K": ITEMS,
"HIT-K": HIT,
"THROW-K": THROW,
"ITEMP-K": ITEMS,
"ITEMR-K": ITEMS,
"MARKDOWN_HELP-K": MARKDOWN_HELP,

#GDPR
"send-gdpr": """Tu información personal ha sido borrada.\n\nTen en cuento que esto no te va a desbanear \
de ningún chat, ya que eso son datos de Telegram, NO datos de YanaBot.
Flooding, advertencias, y bans globales también se conservan, a partir de \
[esto](https://ico.org.uk/for-organisations/guide-to-the-general-data-protection-regulation-gdpr/individual-rights/right-to-erasure/), "
que establece claramente que el derecho de cancelación no se aplica \
\"para la realización de una tarea realizada en interés público.\", así como \
el caso de los datos mencionados anteriormente.""",


#Help modules
"Admin_help": """
 - /adminlist | /admins: Lista os administradores do grupo

*Apenas administradores:*
 - /pin: Afixa silenciosamente a mensagem respondida. Adicione 'loud', 'notify' ou 'violent' para enviar uma notificação aos usuários.
 - /unpin: Desafixa a mensagem atualmente afixada
 - /permanentpin: Defina um PIN permanente para um supergrupo. Quando um canal de administrador ou Telegram altera a mensagem fixada, o bot altera a mensagem fixada imediatamente
 - /invitelink: Obtém o link de convite do grupo
 - /promote: Promove um usuário. Responda ao usuário ou use seu nome de usuário.
 - /demote: Rebaixa um usuário. Responda ao usuário ou use seu nome de usuário.
""",

"AFK_help": """
 - /afk <motivo>: isso marca você como ausente.
 - brb <motivo>: Faz o mesmo que o comando AFK, mas sem ser um comando.

Quando você estiver ausente (AFK), qualquer menção será respondida com uma mensagem informando que você não está disponível.
""",

"Translator_help": """
Este módulo usa o Google Tradutor para fazer as traduções.

 - /tr <language code>: como resposta a uma mensagem longa.
""", 

"Federation_help": """
Ah, gerenciamento de grupo. Tudo é divertido, até que os spammers comecem a entrar no seu grupo e você precise bloqueá-los. Então você precisa começar a banir mais e mais, e dói.
Mas então você tem muitos grupos e não deseja que esses spammers estejam em um de seus grupos - como você pode lidar? Você precisa bloqueá-los manualmente em todos os seus grupos?

Já não! Com as Federações, você pode banir uma pessoa em todos os outros grupos que estão na federação.
Você pode até designar administradores para sua federação, para que seu administrador confiável possa banir pessoa de todos os chats que você deseja proteger.

Ainda na fase experimental, fazer federações só pode ser feito pelo meu criador

*Comandos:*
 - /newfed <nome da fed>: crie uma nova Federação com o nome fornecido. Os usuários só podem ter uma federação. Este método também pode ser usado para renomear a Federação. (máx. 64 caracteres)
 - /delfed: exclua sua Federação e qualquer informação relacionada a ela. Não removerá usuários banidos.
 - /fedinfo <FedID>: informações sobre a Federação especificada.
 - /joinfed <FedID>: coloque seu grupo na Federação. Somente os proprietários de grupos podem fazer isso. Todo grupo pode estar apenas em uma federação.
 - /leavefed <FedID>: saia da Federação dada. Somente os proprietários de grupos podem fazer isso.
 - /fpromote <user>: promova usuários na federação. Somente proprietário da Fed.
 - /fdemote <user>: rebaixa o usuário da federação para um usuário normal.  Somente proprietário da Fed.
 - /fban <user>: bani usuários da federação em que o grupo faz parte, apenas fedadmin tem controle.
 - /unfban <user>: desbani o usuário da federação que o grupo faz parte.
 - /setfrules: organiza as regras da Federação.
 - /frules: veja as regras da federação
 - /chatfed: veja a Federação no chat atual.
 - /fedadmins: mostrar administradores da federação.
 - /fbanlist: exibe todos os usuários fbanidos na federação no momento.
 - /fedchats: obtenha todos os grupos conectados na federação.
 - /importfbans: responda ao arquivo de mensagens de backup da federação para importar a lista de banidos para a federação.
""", 

"Memes and etc._help": """
*Alguns comandos de memes, descubra tudo sozinho!*
- /owo: OWO o texto
- /stretch: ESTICA o texto
- /vapor: torne o texto em vapor
- /hitler: Cite uma mensagem e digite este comando para criar uma legenda para hitler
- /mock: Faz o mesmo que /hitler, mas com o spongemock no lugar.
- /kim: Faz o mesmo que /hitler, mas com Kim Jong Un (ah não por favor não bombardeie minha casa)
- /pidor: 4pda memes
- /zalgofy: Responde uma mensagem para tornar ela um g̫̞l̼̦i̎͡tͫ͢c̘ͭh̛̗
- /deepfry: Para quando você está com fome de memes
- /shout <keyword>: Escreva qualquer coisa que você queira gritar alto
- /dllm: Alguns memes chineses

*Emojis:*
- /clapmoji
- /bmoji
- /copypasta
""", 

"Android_help": """
*Aqui você terá vários comandos úteis para usuários Android!*

*Ferramentas úteis:*
 - /device <codinome>: obtém informações básicas do dispositivo Android a partir de seu codinome
 - /magisk: obtém a versão mais recente do Magisk Estável/Beta/Canary
 - /twrp <codinome>: obtém o twrp mais recente para o dispositivo Android usando seu codinome
 - /specs <marca> <nome do aparelho>: fornecerá as especificações completas de um dispositivo

 *ROM específica para um dispositivo:*
 - /aex <dispositivo> <versão do Android>: Obtenha a ROM AEX mais recente para um dispositivo
 - /bootleggers <device>: Obtenha a ROM Bootleggers mais recente para um dispositivo
 - /dotos <device>: Obtenha a ROM DotOS mais recente para um dispositivo
 - /evo <device>: Obtenha a ROM Evolution X mais recente para um dispositivo
 - /havoc <device>: Obtenha a ROM Havoc mais recente para um dispositivo
 - /los <device>: Obtenha a ROM LineageOS mais recente para um dispositivo
 - /miui <device>: Obtenha a ROM MIUI mais recente para um dispositivo
 - /pe <device>: Obtenha a ROM Pixel Experience mais recente para um dispositivo
 - /pe10 <device>: Obtenha a ROM Pixel Experience (Android 10) mais recente para um dispositivo
 - /peplus <device>: Obtenha a ROM Pixel Experience Plus mais recente para um dispositivo
 - /pearl <device>: Obtenha a ROM Pearl mais recente para um dispositivo
 - /pixys <device>: Obtenha a ROM Pixys mais recente para um dispositivo
 - /posp <device>: Obtenha a ROM POSP mais recente para um dispositivo
 - /viper <device>: Obtenha a ROM ViperOS mais recente para um dispositivo
 
 *GSIs:*
 - /descendant: Obtenha a GSI mais recente do Descendant!
 - /enesrelease: Receba o upload mais recente do Enes!
 - /phh: Receba as últimas GSIs AOSP Oreo do Phh!
""",

"AntiFlood_help": """
 - /flood: te mostra as atuais configurações do controle anti-flood.

*Apenas administradores:*
 - /setflood <int/'no'/'off'>: ativa e desativa o controle anti-flood
""",

"Direct Links_help": """
*Este módulo permite gerar links diretos a partir de vários sites.*

/direct <url>: retornará um link de download direto.

*Lista de URLs suportadas:*
`Google Drive - MEGA.nz - Cloud Mail - Yandex.Disk - AFH - ZippyShare - MediaFire - SourceForge - OSDN - GitHub`
""",

"Antispam security_help": """
*Apenas administradores:*
 - /antispam <on/off/yes/no>: desative ou ative a segurança antispam do grupo ou ele fornecerá suas configurações atuais.

Os proprietários do bot costumam usar antispam para proibir spammers em todos os grupos. Isso ajuda a manter seu grupo seguro. \
eliminando spammers o mais rápido possível. O Anti-Spam pode ser desativado no seu grupo digitando /antispam

*Sistema Anti-Spam do Combot:*
Você pode melhorar sua proteção Antispam usando o comando /setcas para ativar a verificação de novos membros com base no [Combot Anti Spam System](https://combot.org/cas)

*Comandos do CAS:*
 - /casver: Retorna a versão da API que o bot está executando no momento
 - /cascheck: Verifica você ou outro usuário em relação ao CAS Ban

*Apenas administradores:*
 - /setcas <on/off/true/false>: ativa /desativa a verificação do CAS nas boas-vindas
 - /getcas: obtém as configurações atuais do CAS
 - /setban <on/off/true/false>: ativa/desativa o banimento automático em usuários banidos no CAS.

*Apenas Sudo:*
 - /gbanlist: fornecerá a lista completa de usuários banidos globalmente

*Créditos:*
Obrigado ao @nunopenim por fornecer sua API proprietária do Combot Anti Spam System - [(pyCombotCAS_API)](https://github.com/nunopenim/pyCombotCAS_API)
""",

"Bans_help": """
Algumas pessoas precisam ser banidas publicamente; spammers, pessoas irritantes ou apenas trolls.

Este módulo permite que você faça isso facilmente, expondo algumas ações comuns, para que todos vejam!

*Os comandos disponíveis são:*
 - /ban: bane um usuário do seu grupo.
 - /banme: banir-se
 - /tban: bane temporariamente um usuário do seu grupo. Defina o tempo usando <d/h/m> (dias, horas, minutos)
 - /unban: desbane um usuário do seu grupo.
 - /sban: bane silenciosamente um usuário. (via identificador ou resposta)
 - /mute: silencia um usuário no seu grupo.
 - /tmute: silencia temporariamente um usuário em seu grupo. Defina o tempo usando <d/h/m> (dias, horas, minutos)
 - /unmute: dessilencia um usuário do seu grupo.
 - /kick: remove um usuário do seu grupo.
 - /kickme: usuários que usam isso, se removem!

Um exemplo de como silenciar temporariamente alguém:
/tmute @username 2h; isso silencia o usuário por 2 horas.
""",

"Connections_help": """
Às vezes, você só deseja adicionar notas e filtros a um bate-papo em grupo, mas não quer que todos vejam; É aqui que entram as conexões ...

Isso permite que você se conecte ao banco de dados de um bate-papo e adicione coisas a ele sem que as pessoas do grupo saibam disso! Por razões óbvias, você precisa ser um administrador para adicionar coisas; mas qualquer membro pode visualizar seus dados. (usuários banidos/removidos não podem!)

*Ações disponíveis em grupos conectados:*
 • Ver e editar notas
 • Ver e editar filtros
 • Ver e editar lista-negra
 • Promover/rebaixar usuários
 • Ver lista de administradores e link de convite
 • Desativar/ativar comandos no grupo
 • Silenciar/dessilenciar usuários no grupo
 • Restringir/remover restrições de usuários no grupo
 • Mais no futuro!

 - Digite /connect ou /connection no grupo que você deseja se conectar.
 - /connection ou /connect <ID do grupo>: conecte-se ao grupo remoto
 - /disconnect: desconecte-se do grupo
 - /allowconnect on/yes/off/no: permiti que usuários se conectem ao grupo

Você pode obter o ID do grupo usando o comando /id no grupo não se surpreenda se o ID for negativo; todos os super grupos têm IDs negativos.
""",

"Image Lookup_help": """
*Este módulo usa o Google Images para fazer uma pesquisa reversa de imagens.*

- /reverse: Faz uma pesquisa de imagem reversa da mídia à qual foi respondida.
""",

"Filters_help": """
Torne o seu grupo mais animado com filtros; O bot responderá a certas palavras! Os filtros não diferenciam maiúsculas de minúsculas; toda vez que alguém disser suas palavras-chave, Hitsuki responderá outra coisa! pode ser usado para criar seus próprios comandos, se desejado.

 - /filters: lista todos os filtros ativos neste bate-papo.

*Apenas administradores:*
 - /filter <palavra chave> <mensagem de resposta>: Toda vez que alguém diz "palavra", o bot responde com "frase". Para vários filtros de palavras, cite a primeira palavra.
 - /stop <palave chave do filtro>: para o determinado filtro
 
Um exemplo de como definir um filtro seria via:
`/filter Olá Olá! Como você está?`
Um filtro de várias palavras pode ser definido através de:
`/filter "olá amigo" Olá de volta! Há quanto tempo!`
Se você deseja salvar uma imagem, gif ou adesivo ou qualquer outro dado, faça o seguinte:
`/filter palavra`, enquanto responde a um adesivo ou a qualquer dado que você desejar. Agora, toda vez que alguém mencionar "palavra", esse adesivo será enviado como resposta.
""",

"Command disabling_help": """
Nem todo mundo quer todos os recursos que o bot oferece. É melhor deixar alguns comandos sem uso; para evitar spam e abuso.

Isso permite que você desabilite alguns comandos usados ​​com frequência, para que ninguém possa usá-los. Também permitirá que você os exclua automaticamente, impedindo que as pessoas enviem mensagens de texto azul.

 - /cmds: verifique o status atual dos comandos desabilitados

*Apenas administradores:*
 - /enable <nome do cmd>: ativa esse comando
 - /disable <nome do cmd>: desativa esse comando
 - /listcmds: lista todos os possíveis comandos alternáveis
""",

"Dogs and Cats_help": """
*Um módulo para amantes de cães e gatos!*

*Comandos de gatos:*
 - /dog: Envia fotos de cachorros fofos
 - /doghd: Envia imagens de cachorros fofos em alta definição
 - /dogif: Envia gifs de cachorros fofos

*Comandos de cães :*
 - /cat: Envia fotos de gatinhos fofos
 - /cathd: Envia imagens de gatinhos fotos em alta definição
 - /catgif: Envia gifs de gatinhos fotos
""",

"Locks_help": """
Os adesivos te incomodam? Ou deseja evitar que as pessoas compartilhem links? Ou fotos? Você está no lugar certo!

O módulo de travas permite bloquear alguns itens comuns no mundo do Telegram; o bot irá excluí-los automaticamente!

*Os comandos disponíveis são:*
 - /lock <item>: bloqueia o uso de "item". Agora, apenas os administradores poderão usar isso!
 - /unlock <item>: desbloquear "item". Todos podem usá-lo novamente.
 - /locks: lista o status do bloqueio no chat.
 - /locktypes: obtém uma lista de todas as coisas que podem ser bloqueadas.  (Veja isso!)

Ex: bloquear adesivos
/lock sticker
""",

"Log Channels_help": """
*Apenas administradores:*
- /logchannel: Obtém o canal de logs
- /setlog: configura o canal de logs.
- /unsetlog: desativa o canal de logs.

Para configurar um canal de logs é feito da seguinte forma:
 1. Adicione o bot ao canal desejado (como administrador!)
 2. Escreva /setlog no canal.
 3. Encaminhe /setlog para o grupo
""",

"Misc_help": """
*Ferramentas de grupo:*
 - /id: obtenha o ID do grupo atual. Se usado respondendo a uma mensagem, obtém o ID do usuário.
 - /info: obtenha informações sobre um usuário.
 - /gdpr: exclua suas informações do banco de dados do bot. Apenas conversas privadas.
 - /stickerid: responda a um adesivo para que eu diga seu ID de arquivo.
 - /getsticker: responda a um adesivo para fazer o upload do arquivo PNG bruto.
 - /markdownhelp: resumo rápido de como o markdown funciona no Telegram - só pode ser usado em chat privado.

*Ferramentas úteis:*
 - /git: Retorna informações sobre um usuário ou organização do GitHub.
 - /repo: Retornar a lista de repositórios de usuários ou organizações do GitHub (Limitado em 40)
 - /lyrics: Encontre suas letras de músicas favoritas!
 - /paste: Crie uma pasta ou um URL abreviado usando o [dogbin](https://del.dog)
 - /getpaste: Obtenha o conteúdo de uma pasta ou URL abreviado do [dogbin](https://del.dog)
 - /pastestats: Obter estatísticas de uma pasta ou URL abreviado do [dogbin](https://del.dog)
 - /ud: Digite a palavra ou expressão que deseja pesquisar. Por exemplo /ud Gay
 - /removebotkeyboard: Tem um teclado de bot desagradável preso no seu grupo?
 - /exec <language> <code> [/stdin <stdin>]: Execute um código em uma língua especificada. Envie um comando vazio para obter as linguagens suportadas.
 - /wiki <palavras>: Obtenha artigos da Wikipedia apenas usando este bot!

*Outras coisas:*
 - /runs: responde uma sequência aleatória de uma matriz de respostas.
 - /insults: responde uma sequência aleatória de uma matriz de respostas.
 - /slap: dar um tapa em um usuário ou se dar um tapa se não for uma resposta.
 - /decide: Responde aleatoriamente entre yes/no/maybe.
""",

"Purges_help": """
*Exclua mensagens facilmente com este comando. Bot limpa mensagens todas juntas ou individualmente.*

*Apenas administradores:*
 - /del: exclui a mensagem para a qual você respondeu
 - /purge: exclui todas as mensagens entre a resposta do comando e a mensagem.
 - /purge <X inteiro>: exclui a mensagem respondida e X mensagens após ela.
""",

"Damain Blacklists_help": """
A lista negra de domínios é usada para impedir que determinados domínios sejam mencionados em um grupo. Sempre que um URL desse domínio for mencionado, a mensagem será excluída imediatamente.

*NOTA:* a lista negra de domínios não afeta os administradores do grupo.

- /geturl: Exibe os URLs atuais da lista negra

*Apenas administradores:*
- /addurl <urls>: Adicione um domínio à lista negra. O bot analisará automaticamente o URL.
- /delurl <urls>: Remove os URLs da lista negra
""",

"Backups_help": """
*Apenas para os administradores do grupo:*

 - /import: responda ao arquivo de backup de grupo do butler/emilia para importar o máximo possível, facilitando muito as transferências! Observe que arquivos/fotos não podem ser importados devido a restrições de Telegram.

 - /export: exportar dados do grupo.  Os dados exportados incluem regras, notas (documentos, imagens, música, vídeo, áudio, voz, texto, botões de texto), listas negras, comandos e bloqueios. Mais virá gradualmente!

*Este módulo ainda está na versão beta!*
""",

"Reactions_help": """
*Use estes comandos para deixar o bot expressar reações por você!*

 - /react: reage com reações normais.
 - /happy: reage com felicidade.
 - /angry: reage com raiva.
""",

"Notes_help": """
*Salve dados para futuros usuários com notas!*
*As notas são ótimas para salvar petiscos aleatórios de informações; um número de telefone, um belo gif, uma imagem engraçada - qualquer coisa!*

*Os comandos disponíveis são:*
 - /save <palavra> <sentença>: Salve essa frase na nota chamada "palavra". Responder a uma mensagem salvará essa mensagem. Funciona até com mídias!
 - /get <palavra>: receba a nota salva nessa palavra.
 - #<word>: o mesmo que /get palavra
 - /clear <palavra>: apaga a nota chamada "palavra"
 - /notes: lista todas as notas no chat atual
 - /saved: o mesmo que /notes

Um exemplo de como salvar uma nota seria via:
/save data Estes são alguns dados!
Agora, qualquer pessoa que use "/get data" ou "#data" será respondida com "Estes são alguns dados!!".
Se você deseja salvar uma imagem, gif ou adesivo ou qualquer outro dado, faça o seguinte:
/save palavra enquanto responde a um adesivo ou a qualquer dado que você desejar. Agora, a nota em "#palavra" contém um adesivo que será enviado como resposta.

*Dica:* para recuperar uma anotação sem a formatação, use /get <nome da nota> noformat
Isso recuperará a nota e a enviará sem formatá-la; obtendo o markdown bruto, permitindo que você faça edições fáceis.

*Nota:* Os nomes das notas não diferenciam maiúsculas de minúsculas e são convertidos automaticamente em minúsculas antes de serem salvos.
""",

"Reporting_help":"""
 - /report <razão>: responda a uma mensagem para denunciá-la aos administradores.
 - @admin: responda a uma mensagem para denunciá-la aos administradores.
*NOTA:* nenhum desses itens será acionado se usado pelos administradores

*Apenas administradores:*
 - /reports <on/off>: altera a configuração do denúncias ou exibi o status atual.
   - Se feito no PV, alterna seu status.
   - Se feito no grupo, alterna o status do grupo.
""",

"Rules_help": """
*Defina regras para organizar seu grupo, mas não faça dele uma ditadura!*

 - /rules: Obtenha as regras de um grupo.

*Apenas administradores:*
 - /setrules <regras>: Define as regras para um grupo.
 - /clearrules: apague as regras de um grupo.
""",

"Sed/Regex_help": """
 - s/<text1>/<text2>(/<flag>): Responda a uma mensagem com isso para executar uma operação sed nessa mensagem, substituindo todas as ocorrências de 'texto1' com 'texto2'. Os sinalizadores são opcionais e atualmente incluem 'i' para ignorar maiúsculas e minúsculas, 'g' para global ou nada.  Os delimitadores incluem `/, _, |,` e `: .` O agrupamento de texto é suportado. A mensagem resultante não pode ser maior que 4096.
 
*Lembrete:* Sed usa alguns caracteres especiais para facilitar a correspondência, como estes: `+ *.? \`
 Se você quiser usar esses caracteres, escape deles!
 por exemplo: `\\?.`
""",

"Warnings_help": """
 - /warns <userhandle>: Mostra o número de avisos e os motivos em relação ao usuário a quem você responde
 - /warnlist: lista de filtros de aviso atuais.

*Apenas administradores:*
 - /warn <userhandle>: avisa um usuário. Após três avisos, o usuário será banido do grupo. Pode ser usado em resposta a uma mensagem.
 - /resetwarn <userhandle>: Redefina os avisos para um usuário. Pode ser usado em resposta a uma mensagem.
 - /addwarn <palavrachave> <mensagem adicionada>: defina um filtro de aviso em uma palavra-chave específica. Se você quiser sua palavra-chave \
 seja uma frase, coloque-a entre aspas, como aqui: `/addwarn "muito puto" Este é um usuário irritado`.
 - /nowarn <palavrachave>: parar um filtro de aviso
 - /warnlimit <num>: defina o número máximo de avisos
 - /strongwarn <on/yes/off/no>: Se estiver ativado e o número de avisos for excedido, o usuário será banido. Caso contrário, a pessoa só será expulsa
""",

"Greetings_help": """
*Dê a seus membros uma recepção calorosa com o módulo de cumprimentos! Ou um triste adeus... Depende!*

*Os comandos disponíveis são:*
 - /welcome <on/off/yes/no>: ativa/desativa as mensagens de boas-vindas. Se nenhuma opção for fornecida, retornará para o padrão a mensagem de boas-vindas e as configurações de boas-vindas.
 - /goodbye <on/off/yes/no>: ativa/desativa as mensagens de despedida. Se nenhuma opção for fornecida, retorna as configurações atuais da mensagem de despedida.
 - /setwelcome <mensagem>: define uma nova mensagem de boas-vindas! Markdown e botões são suportados, bem como recheios.
 - /resetwelcome: redefine a mensagem de boas-vindas para o padrão; excluindo as alterações que você fez.
 - /setgoodbye <mensagem>: define uma nova mensagem de despedidas! Markdown e botões são suportados, bem como recheios.
 - /resetgoodbye: redefina a mensagem de despedida para o padrão; excluindo as alterações que você fez.
 - /cleanservice <on/off/yes/no>: exclui todas as mensagens de serviço; esses são os irritantes "x entrou no grupo" que você vê quando as pessoas entram.
 - /cleanwelcome <on/off/yes/no>: exclui antigas mensagens de boas-vindas;  quando uma nova pessoa entra no grupo, a mensagem de boas-vindas anterior é excluída.
 - /welcomemute <on/off/yes/no>: todos os usuários que entram no grupo são silenciados;  um botão é adicionado à mensagem de boas-vindas para que eles sejam dessilenciados. Isso prova que eles não são um robô!
 - /welcomemutetime <Xw/d/h/m>: se um usuário não pressionar o botão "clique para provar que você é humano" na mensagem de boas-vindas após um certo período de tempo, será dessilenciado automaticamente após esse período.
 Nota: se desejar redefinir o tempo do mudo para sempre, use /welcomemutetime 0m. 0 == infinito!
 - /setmutetext <novo texto>: Personalize o botão "clique aqui para provar que você é humano" obtido da ativação do welcomemute.
 - /resetmutetext: redefine o botão de silenciar para o texto padrão.

Leia o /markdownhelp para aprender sobre como formatar seu texto e mencionar novos usuários quando entrarem no grupo!

*Recheios:*
Como mencionado, você pode usar determinadas tags para preencher sua mensagem de boas-vindas com informações de usuário ou bate-papo; essas são:
{first}: O primeiro nome do usuário.
{last}: O sobrenome do usuário.
{fullname}: O nome completo do usuário.
{username}: O nome de usuário do usuário;  se nenhum estiver disponível, menciona o usuário.
{mention}: Menciona o usuário, usando seu primeiro nome.
{id}: O ID do usuário.
{chatname}: O nome do grupo.

Um exemplo de como usar recheios seria definir as boas-vindas, via:
/setwelcome Olá, {first}! Bem-vindo ao {chatname}.

Você pode ativar/desativar as mensagens de boas-vindas da seguinte forma:
/welcome off

Se você deseja salvar uma imagem, gif ou adesivo ou qualquer outro dado, faça o seguinte:
/setwelcome enquanto responde a um adesivo ou a qualquer dado que você desejar. Esses dados agora serão enviados para receber novos usuários.

*Dica:* use /welcome noformat para recuperar a mensagem de boas-vindas não formatadaz.
Isso recuperará a mensagem de boas-vindas e a enviará sem formatação; obtendo o markdown bruto, permitindo que você faça edições fáceis.
Isso também funciona com /goodbye.
"""
}