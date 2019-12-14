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
    "{user1} {throws} {item} a {user2}.",
    "{user1} {throws} {item} na cara do {user2} .",
    "{user1} joga na cabeça a {item} no {user2}.",
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
    "arremessar",
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
Markdown es una herramienta de formato muy poderosa soportada por telegram. {} tiene algunas mejoras, para asegurarse de que \
las notas guardadas se analizan correctamente y te permiten crear botones..

- <code>_cursiva_</code>: si se introduce el texto entre '_' generará texto en cursiva
- <code>*negrita*</code>: si se introduce el texto entre '*' generará texto en negrita
- <code>`codigo`</code>: si se introduce el texto entre '`' generará texto monoespaciado, también conocido como 'código'
- <code>[algúntexto](algunaURL)</code>: esto creará un link - el mensaje se mostrará en <code>algúntexto</code>, \
y pulsando en el te llevará a la página que has puesto en <code>algunaURL</code>.
EJ: <code>[test](example.com)</code>

- <code>[textodelboton](buttonurl:algunaURL)</code>: esta es una mejora especial que permite a los usuarios \
tener botones de telegram. <code>textodelboton</code> será el nombre que aparezca en el botón, y <code>algunaURL</code> \
será la página web o URL que se abrirá al pulsar.
EG: <code>[Esto es un botón](buttonurl:example.com)</code>

Si quieres poner varios botones en la misma línea, usa :same, como aquí:
<code>[uno](buttonurl://example.com)
[dos](buttonurl://google.com:same)</code>
Esto creará dos botones en la misma línea en vez de uno en cada línea.
"""

PortugueseBrStrings = {

#Connections
    "Disabled connections to this chat for users": "Conexiones deshabilitadas en este chat para los usuarios",
    "Enabled connections to this chat for users": "Conexiones habilitadas en este chat para los usuarios",
    "Please enter on/yes/off/no in group!": "Por favor escribe on/yes/off/no en el grupo!",
    "Successfully connected to *{}*": "Conectado correctamente a *{}*",
    "Connection failed!": "Conexión fallida!",
    "Connections to this chat not allowed!": "Conexiones no permitidas en este chat!",
    "Write chat ID to connect!": "Escribe el ID del chat para conectar!",
    "Usage limited to PMs only!": "Uso restringido solo a mensajes privados",

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
    "\nPermanent user link: {}": "\nLink do usuário: {}",
    "\n\nThis person is my owner - I would never do anything against them!":
        "\n\nEssa pessoa é minha dono(a), eu nunca faria algo contra ela!",
    "\nThis person is one of my sudo users! Nearly as powerful as my owner - so watch it.":
        "\nEssa pessoa é um dos meus usuários Sudo! Tem quase tanto poder quanto meu dono, então tenha cuidado",
    "\nThis person is one of my support users! Not quite a sudo user, but can still gban you off the map.":
        "\nEssa pessoa é um dos meus usuários suporte. Não é como um usuário sudo, mas pode te banir globalmente, tenha cuidado!",
    "\nThis person has been whitelisted! That means I'm not allowed to ban/kick them.":
        "\nEssa pessoa está na lista branca. Isso significa que eu não posso banir ou removê-la.",

    "Its always banhammer time for me!": "É sempre a hora do martelo do ban para mim!",

    "It's {} in {}": "Está {} em {}",

    "Please reply to a sticker to get its ID.": "Por favor responda a um stickerer para obeter o seu ID.",
    "Please reply to a sticker for me to upload its PNG.": "Por favor, responda a um sticker para que eu possa upar seu PNG .",

    "Write a location to check the weather.": "Escribe una ubicación para ver que tiempo hace.",
    "I will keep an eye on both happy and sad times!": "Estaré aquí en las buenas y en las malas!",
    "Today in {} is being {}, around {}°C.\n": "Hoy en {} hace {}, alrededor de {}°C.\n",
    "Sorry, location not found.": "Lo siento, ubicación no encontrada.",

    "Deleting identifiable data...": "Borrando datos de usuario...",

    "Try forwarding the following message to me, and you'll see!":
        "Prueba a enviarme el siguiente mensaje y lo verás!",
    "/save test This is a markdown test. _italics_, *bold*, `code`, [URL](example.com) [button](buttonurl:github.com) [button2](buttonurl://google.com:same)":
    """/save test Esto es un test de markdown. _cursiva_, *negrita*, `codigo`, \
[URL](example.com) 
[Botón](buttonurl:github.com)
[Botón2](buttonurl://google.com:same)""",

#Misc GDPR
"send-gdpr": """Tu información personal ha sido borrada.\n\nTen en cuento que esto no te va a desbanear \
de ningún chat, ya que eso son datos de Telegram, NO datos de YanaBot.
Flooding, advertencias, y bans globales también se conservan, a partir de \
[esto](https://ico.org.uk/for-organisations/guide-to-the-general-data-protection-regulation-gdpr/individual-rights/right-to-erasure/), "
que establece claramente que el derecho de cancelación no se aplica \
\"para la realización de una tarea realizada en interés público.\", así como \
el caso de los datos mencionados anteriormente.""",

#Admin
"How am I meant to promote someone that's already an admin?": "¿Como voy a ascender a administrador a alguien que ya lo es?",
"I can't promote myself! Get an admin to do it for me.": "¡No puedo hacerme administradora a mi misma! ¡Avisa a algún administrador para que lo haga!",
"Successfully promoted in *{}*!": " Ascendido a administrador en *{}*!",

"This person CREATED the chat, how would I demote them?": "Esta persona ha creado el chat. ¿Cómo quieres que le quite el admin?",
"Can't demote what wasn't promoted!": "No puedo quitarle el admin si no lo tiene!",
"I can't demote myself!": "No puedo quitarme de ser administradora yo misma!",
"Successfully demoted in *{}*!": "Ya no es administrador en *{}*!",
"Could not demote. I might not be admin, or the admin status was appointed by another user, so I can't act upon them!": 
"No puedo quitarle el admin. Puede que no sea administrador o que el estado de administrador fuese dado por otro usuario, asi que no puedo actuar sobre él!",

"I don't have access to the invite link, try changing my permissions!": "No tengo acceso al link de invitación, prueba cambiando mis permisos!",
"I can only give you invite links for supergroups and channels, sorry!": "Lo siento, solo puedo dar links de invitación para supergrupos y canales.",

"Admins in": "Administradores em",
"this chat": "este chat",
" (Creator)": " (Criador)",

#AFK
"{} is now AFK!": "Agora {} está AFK!",
"{} is no longer AFK!": "{} Não está AFK!",
"{} is AFK!": "{} está AFK!",
"{} is AFK! says its because of: \n{}": "{} está AFK! Disse que é por causa: \n{}",

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
    "<b>Current blacklisted words in {}:</b>\n": "<b>Palabras en la lista negra en {}:</b>\n",
    "There are no blacklisted messages in <b>{}</b>!": "No hay mensajes en la lista negra en <b>{}</b>!",
    "Added <code>{}</code> to the blacklist in <b>{}</b>!":
        "Añadido <code>{}</code> a la lista negra en <b>{}</b>!",
    "Tell me which words you would like to add to the blacklist.":
        "Dime qué palabras te gustaría añadir a la lista negra.",
    "Removed <code>{}</code> from the blacklist in <b>{}</b>!":
        "Borrado <code>{}</code> de la lista negra en <b>{}</b>!",
    "This isn't a blacklisted trigger...!": "Este no es un comando de la lista negrа...!",
    "None of these triggers exist, so they weren't removed.":
        "Ninguno de estos comandos existía, asi que no han sido borrados.",
    "Removed <code>{}</code> triggers from the blacklist in <b>{}</b>! {} did not exist, so were not removed.":
        "Borrado <code>{}</code> de los comandos de la lista negra en <b>{}</b>! {} no existe, así que no ha sido borrado!.",
    "Tell me which words you would like to remove from the blacklist.":
        "Dime que palabras te gustaría borrat de la lista negra.",

    #Filters
    "*Filters in {}:*\n": "*Filtros en {}:*\n",
    "local filters": "filtros locais",
    "*local filters:*\n": "*filtros locales:*\n",
    "No filters in {}!": "No tem filtros em {}!",
    "There is no note message - You can't JUST have buttons, you need a message to go with it!":
        "No hay mensaje - No puedes tener botones vacíos, necesitas un mensaje que vaya dentro del botón!",
    "You didn't specify what to reply with!": "No has especificado con qué quieres que responda!",
    "Handler '{}' added in *{}*!": "El filtro '{}' ha sido añadido en *{}*!",
    "No filters are active in {}!": "No hay filtros activos en {}!",
    "Yep, I'll stop replying to that in *{}*." : "Valee, dejaré de responder a eso en *{}*.",
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
        "No he podido borrar todos los mensajes. Puede que los mensajes sean muy viejos, que no tenga derechos para borrarlos o que esto no sea un supergrupo.",
    "Purge complete.": "Purga completada.",
    "Reply to a message to select where to start purging from.":
        "Responde a un mensaje para seleccionar desde donde empezar la purga.",
    "Whadya want to delete?": "¿Qué quieres borrar?",

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
    "Get rekt": "¡Te destrozo!.",


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
        "Purges": "Expurgor",
        "Muting & Restricting": "Silenciar e restringir",
        "Notes": "Notas",
        "Reporting": "Reportar",
        "RSS Feed": "Feed RSS",
        "Rules": "Regras",
        "Connections": "Conexões",
        "Bios and Abouts": "Biografia",
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

"send-start": """Hola {}, me llamo {}! Si tienes alguna pregunta sobre como usarme, lee /help - y después ve a @NotAvaibleYet.

Soy un bot para administrar grupos mantenido por [esta maravillosa persona](tg://user?id={}). Soy parecida a [Marie](https://github.com/PaulSonOfLars/tgbot) 
Estoy hecha python3, usando la librería de \
python-telegram-bot, y soy totalmente de codigo abierto - puedes ver lo que me hace funcionar \
[aquí](https://gitlab.com/MrYacha/pYanaBot-2.0)!

Siéntete libre para enviar propuestas en GitHub, o contactar con mi creador en mi grupo de soporte, @YanaBotGroup, con los bugs, preguntas \
o propuestas defunciones que puedas tener :)

Si te gusta usarme, y/o me quieres ayudar a sobrevivir a las tempestades, presiona /donate para ayudar a pagar/actualizar mi VPS!
""",

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
você tem interesse""",

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
 - /adminlist | /admins: lista os administradores de este chat

*Apenas administradores*
 - /pin: Ancla silenciosamente el mensaje respondido: agrega 'loud' o 'notify' para notificar a los usuarios.
 - /unpin: Desancla en mensaje anclado
 - /invitelink: Genera el link de invitación al grupo
 - /promote: Asciende a administrador al usuario al que se le responde
 - /demote: Quita el administrador al usuario al que se le responde
""",

"AFK_help": """
 - /afk <motivo>: isso marca você como ausente.
 - brb <motivo>: Faz o mesmo que o comando AFK, mas sem ser um comando.

Quando você estiver ausente (AFK), qualquer menção será respondida com uma mensagem informando que você não está disponível.
""",

"Android_help": """
*Aqui você terá vários comandos úteis para usuários do Android!*

*Ferramentas úteis:*
 - /device <codinome>: obtém informações básicas do dispositivo Android a partir de seu codinome
 - /magisk: obtém a versão mais recente do Magisk Estável/Beta/Canary
 - /twrp <codinome>: obtém o twrp mais recente para o dispositivo Android usando o codinome
 - /specs <marca> <nome do aparelho>: fornecerá as especificações completas de um dispositivo

 *ROM específica para um dispositivo:*
 - /aex <dispositivo> <versão do Android>: Obtenha a ROM AEX mais recente para um dispositivo
 - /bootleggers <device>: Obtenha a ROM mais recente da Bootleggers para um dispositivo
 - /dotos <device>: Obtenha a última ROM da DotOS para um dispositivo
 - /evo <device>: Obtenha a versão mais recente da ROM Evolution X para um dispositivo
 - /havoc <device>: Obtenha a ROM Havoc mais recente para um dispositivo
 - /los <device>: Obtenha a ROM mais recente da LineageOS para um dispositivo
 - /miui <device>: Obtenha a ROM MIUI mais recente para um dispositivo
 - /pe <device>: Obtenha a ROM mais recente da Pixel Experience para um dispositivo
 - /pe10 <device>: Obtenha a ROM mais recente da Pixel Experience 10 para um dispositivo
 - /peplus <device>: Obtenha a ROM mais recente da Pixel Experience Plus para um dispositivo
 - /pearl <device>: Obtenha a mais recente ROM Pearl de um dispositivo
 - /pixys <device>: Obtenha a ROM Pixys mais recente de um dispositivo
 - /posp <device>: Obtenha a ROM POSP mais recente para um dispositivo
 - /viper <device>: Obtenha a ROM mais recente da Viper para um dispositivo
 
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
 - /kickme: remove a pessoa que usa o comando

*Apenas administradores:*
 - /ban <userhandle>: banea a un usuario. (via nombre de usuario, o respondiendo a un mensaje suyo)
 - /tban <userhandle> x(m/h/d): banea a un usuario durante x tiempo. (via nombre de usuario, o respondiendo a un mensaje suyo). m = minutos, h = horas, d = días.
 - /unban <userhandle>: desbanea a un usuario. (via nombre de usuario, o respondiendo a un mensaje suyo)
 - /kick <userhandle>: expulsa a un usuario, (via nombre de usuario, o respondiendo a un mensaje suyo)
""",

"Connections_help": """
Acciones disponibles mediante grupos conectados:
 • Ver y editar notas
 • Ver y editar filtros
 • Ver y editar la lista negra
 • Ascender/quitar administrador
 • Ver la lista de administradores, ver link de invitación
 • Desactivar/activar comandos en el chat
 • Silenciar/quitar silencio a usuarios en el chat
 • Restringir/quitar restricción a usuarios en el chat
 • ¡Más en el futuro!

 - /connection <iddelchat>: Conecta al chat remoto
 - /disconnect: Desconecta del chat
 - /allowconnect on/yes/off/no: Permite a los usuarios conectarse al grupo
""",

"Filters_help": """
Torne o seu bate-papo mais animado com filtros; O bot responderá a certas palavras!
Os filtros não diferenciam maiúsculas de minúsculas; toda vez que alguém disser suas palavras-chave, {} responderá outra coisa! pode ser usado para criar seus próprios comandos, se desejado.
 - /filters: lista todos os filtros ativos no bate-papo.
*Apenas Admins:*
 - /filter <palavra> <responda a mensagem>: Toda vez que alguém diz "palavra", o bot responde com "frase". Para vários filtros de palavras, cite a primeira palavra.
 - /stop <palavra usada no filtro>: Para (apaga) um filtro.
 
""",

"Command disabling_help": """
 - /cmds: comprueba el estado actual de los comandos deshabilitados.

*Solo administradores:*
 - /enable <nombre comando>: activa ese comando
 - /disable <nombre comando>: desactiva ese comando
 - /listcmds: lista de todos los comandos que se pueden activar o desactivar
""",

"Locks_help": """
 - /locktypes: lista de todos los tipos de bloqueo posibles

*Solo administradores:*
 - /lock <tipo>: bloquea elementos de un determinado tipo (no disponible en chat privado)
 - /unlock <tipo>: desbloquea elementos de un determinado tipo (no disponible en chat privado)
 - /locks: muestra la lista actual de bloqueos en el chat

Los bloqueos se pueden utilizar para restringir a los usuarios de un grupo.
ej:
Bloquear URL borrará automaticamente todos los mensajes que contengan URLs y que no hayan sido metidos en la lista blanca, bloquear stickers borrará todos los \
stickers, etc.
Bloquear los bots hará que ningun usuario no administrador pueda añadir bots al chat.
""",

"Log Channels_help": """
*Solo administradores:*
- /logchannel: Obtém o canal de logs
- /setlog: configura o canal de logs.
- /unsetlog: elimina o canal de logs.

Para configurar um canal de registro se faz da seguinte forma:
- adicione o bot ao canal desejado (como administrador!)
- escreva /setlog no canal
- envie /setlog no grupo
""",

"Misc_help": """
 - /id: obtiene la id del grupo. Si se usa respondiendo a un mensaje, obtiene la id de ese usuario.
 - /runs: responde una frase aleatoria de una batería de frases preestablecidas.
 - /slap: abofetea a u usuario, o recibe una bofetada si no lo utilizas como respuesta.
 - /time <lugar>: te da la hora para el lugar indicado.
 - /weather <ciuidad>: muestra el tiempo climatológico para la ciudad indicada.
 - /info: obtiene información de un usuario.
 - /gdpr: borra tu información de la base de datos del bot. Solo en privado.
 - /stickerid: responde a un sticker con esto y te diré la ID del archivo.
 - /getsticker: responde a un sticker con esto y subiré el archivo en PNG.

 - /markdownhelp: resumen rápido de como funciona el markdown en telegram - solo se puede usar en chats privados.
""",

"Purges_help": """
*Solo administradores:*
 - /del: borra el mensaje al que respondes.
 - /purge: borra todos los mensajes que haya desde el final hasta el mensaje al que respondas.
 - /purge <número X>: borra el mensaje al que respondes, y los X mensajes siguientes.
""",

"Muting & Restricting_help": """
*Solo administradores:*
 - /mute <userhandle>: silencia un usuario. Puede ser usado respondiendo a un mensaje, silenciando al usuario al que respondes.
 - /tmute <userhandle> x(m/h/d): silencia a un usuario durante x tiempo.(via nombre de usuario, o respondiendo a un mensaje suyo). m = minutos, h = horas, d = días.
 - /unmute <userhandle>: quita el silencio a un usuario. Puede ser usado como respuesta, quitando el silencio a usuario al que respondes.
 - /restrict <userhandle>: restringe a un usuario para enviar stickers, gif, links o media. Puede ser usado como respuesta, restringiendo al usuario al que respondes.
 - /trestrict <userhandle> x(m/h/d): restringe a un usuario durante x tiempo. (via nombre de usuario, o respondiendo a un mensaje suyo). m = minutos, h = horas, d = días.
 - /unrestrict <userhandle>: quita la restricción a un usuario para enviar stickers, gif, links o media. Puede ser usado como respuesta, quitando la restricción al usuario al que respondes..
""",

"Notes_help": """
 - /get <nombredelanota>: obtienes la nota guardada con este nombre
 - #<nombredelanota>: lo mismo que con /get
 - /notes o /saved: lista de todas las notas guardadas en el chat.

Si quieres recuperar el contenido de una nota sin formato, utiliza `/get <nombredelanota> noformat`. Esto puede \
ser util cuando actualizas una nota, sobre todo si hay botones en ella.

*Solo administradores:*
 - /save <nombredelanota> <contenidodelanota>: guarda 'contenidodelanota' como nota con el nombre 'nombredelanota'
Se puede añadir botones a las notas usando la sintaxis normal de 'markdown' - el link que añadas al boton deberá llevar antes \
`buttonurl:` tal como se muestra aquí: `[textodelbotón](buttonurl:tulink.com)`. Así quedaria configurado un botón en una nota. Mira /markdownhelp para más información.
 - /save <nombredelanota>: guarda el mensaje al que respondes con 'nombredelanota'
 - /clear <nombredelanota>: borra la nota con ese nombre
""",

"Reporting_help":"""
 - /report <motivo>: responde a un mensaje para reportarlo a los administradores.
 - @admin: responde a un mensaje para reportarlo a los administradores.
NOTA: ninguno de estos comandos se activará si es utilizado por los administradores

*Solo administradores*
 - /reports <on/off>: cambia la configuración de los reportes, o te permite ver el estado actual de la configuración.
   - Si se hace en mensaje privado, cambia tu estado
   - Si se hace en un chat, cambia el estado del chat.
""",

"RSS Feed_help": """
 - /addrss <link>: añade un link RSS a las suscripciones.
 - /removerss <link>: quita un link RSS de las suscripciones.
 - /rss <link>: muestra los datos del link y la ultima entrada, sirve sobre todo para hacer tests.
 - /listrss: muestra la lista de los feeds RSS a los que el chat está suscrito.

NOTA: En grupos, solo los administradores pueden añadir/borrar links RSS a las suscripciones del grupo.
""",

"Rules_help": """
 - /rules: te muestra las normas para ese chat

*Solo administradores:*
 - /setrules <tus normas aquí>: configura las reglas de un chat.
 - /clearrules: borra las reglas para el chat en el que estás.
""",

"Sed/Regex_help": """
 - s/<text1>/<text2>(/<flag>): Responde a un mensaje con esto para hacer una operación sed en ese mensaje, cambiando todas \
las cosas de 'text1' con 'text2'. Flags son opcionales, y actualmente incluyen 'i' para ignorar, 'g' para global, \
o nada. Los delimitadores incluyen `/`, `_`, `|`, y `:`. Se admite la agrupación de texto. El mensaje resultante no puede ser \
más largo de {}.

*Recordatorio:* Sed usa algunos caracteres especiales para facilitar la comparación, como estos: `+*.?\\`
Si quieres usar estos caracteres, asegúrate de que no los incluyes!
eg: `\\?`.
""",

"Warnings_help": """
 - /warns <userhandle>: te muestra el número de avisos y la razón del usuario al que respondes
 - /warnlist: lista de los filtros de avisos actual.

*Solo administradores:*
 - /warn <userhandle>: advierte a un usuario. Despues de 3 advertencias, el usuario será baneado del grupo. Se puede usar respondiendo a un mensaje.
 - /resetwarn <userhandle>: Resetea las advertencias para un usuario. Puede ser usado como respuesta a un mensaje.
 - /addwarn <palabraclave> <mensaje añadido>: establece un filtro de advertencia en una determinada palabra clave. Si quieres que tu palabra clave \
ser una oración, ponla entre comillas, como aquí: `/addwarn "muy enfadado" Esto es un usuario enfadado`. 
 - /nowarn <palabraclave>: detiene un filtro de advertencia
 - /warnlimit <num>: establece el numero de advertencias
 - /strongwarn <on/yes/off/no>: Si está en on y se excede el numero de advertencias, el usuario será baneado. Si no solo será expulsado
""",

"Greetings_help": """
Tus mensajes de Bienvenida/despedida en el grupo se pueden personalizar de múltiples formas. Si quieres que los mensajes sean individualizados \
como mensaje predefinido, sigue estos pasos:
 - `{{first}}`: esto representa el *nombre* del usuario
 - `{{last}}`: esto representa el *apellido* del usuario. Predefinido a *nombre* si el usuario no tiene apellido.
 - `{{fullname}}`: esto representa el nombre *completo*. Por defecto *nombre* del usuario unicamente, si no tiene apellido.
 - `{{username}}`: esto representa el *alias*. Por defecto *meciona* el nombre del usuario si no tiene alias.
 - `{{mention}}`: esto solo *menciona* a un usuario - escribiendo unicamente su nombre.
 - `{{id}}`: esto representa el *id* de usuario.
 - `{{count}}`: esto representa el *numero de miembro*.
 - `{{chatname}}`: esto representa el *nombre del grupo actual*.
Cada variable DEBE ser metida entre `{{}}` para que sea reemplazada.
Los mensajes de bienvenida soportan markdown, asi que puedes hacer que cualquier palabra vaya en negrita/cursiva/monoespaciado/links. \
También puedes poner botones, asi puedes hacer que las bienvenidas queden espectaculares con botones de introducción. \
Para crear un botón que lleve a tus normas, usa esto: `[Normas](buttonurl://t.me/{}?start=group_id)`. \
Simplemente reemplaza el `group_id` con la ID de tu grupo, que puedes obtener via /id, y ya estaría. \
Ten en cuenta que las id de grupo suelen ir precedidas del signo `-`; Ese signo ES NECESARIO, así que por favor \
no lo borres. \
Si tienes el humor suficientes puedes tambien poner imágenes/videos/gif/notas de voz como mensaje de bienvenida,\
respondiendo al mensaje con la imagen/gif/video mediante /setwelcome.

*Solo administradores:*
 - /welcome <on/off>: activa/desactiva ativa e desativa as mensagens de boas vindas.
 - /welcome: mostra a mensagem de boas vindas atual.
 - /welcome noformat: mostra a mensagem de boas vindas atual sem markdown - útil se queres editar uma mensagem de boas vindas!
 - /goodbye -> lo mismo que para /welcome.
 - /setwelcome <alguntexto>: configura tu mensaje de bienvenida. Si se usa respondiendo a media, establece la imagen/gif/video como bienvenida.
 - /setgoodbye <alguntexto>: lo mismo que /setwelcome pero para despedidas.
 - /resetwelcome: resetea el mensaje de bienvenida al mensaje por defecto.
 - /resetgoodbye: resetea el mensaje de despedida al mensaje por defecto.
 - /cleanwelcome <on/off>: Para los nuevos miembros que entran, intenta borrar los mensajes de bienvenida previos, así evita el spam de mensajes de bienvenida en el chat.
 - /cleanservice <on/off/yes/no>: borra los mensajes de servicio; esos mensajes tal que "x se ha unido al grupo" que se ven cuando alguien se une.
 - /welcomesecurity <off/soft/hard>: soft - restringe los permisos del usuario que acaba de entrar, de tal forma que no puede enviar media durante 24 horas, hard - restringe los permisos del usuario para enviar mensages hasta que hace click en el mensaje de \"No soy un bot.\"
"""
}