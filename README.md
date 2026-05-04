```
                           =                      
  ~                        ~                  .   
             ..,,:::::::,,.~..              .+,+..
.         ..:&&&&&&&&####&&&#,..         .*..,:. ~
       .:&&&&###OOoxxOxxxoxoO###:..  .  ...:.&&,~ 
     ,###Ox*??+x?x+++*:::~=?*=xxOO&.?...   ..~~.  
~.~,Ox+~*~*:+:~,,~:=,,?+,,=~~?~?*+*OO.       ,,.  
,.~&==,&&,::++,#&~&&,=~:~,,~:~~+~~=+oO.      x&.  
..==~....,..,x&&&=&*,,~+#o&:=,::=o~=+xO.     +&.  
~O?:~.x~=,:..:~+,,*:.,,~,,::~:+::=~=~#x?     .,.  
.?,.:  ,  . ,.+,~~,,..=,,,,~+ox==,:+*=**.    &&. :
.,:o= , .&..=..:=,,.,+,,,,,,:+++:~:=~~+*.    :~..=
 .,,:::,.,~..~...~.,,.==:&=,,,::::=~:~~?.    &&.  
 :~,..#.,.....~= .:,.===*&x,:,#~+:,:.,,+:    =,.  
.~:O+?+,::~,~~~,=,::.,~,:~:::.,,:,:,~==:O.        
:=:,o=~,,,:o:,,..,,~:=~:=+==+~:,,.,.,~==+,   ..   
::~o+?:o:,,=,.,.,,?x*x?x+&#*==:=,,=OO**=o    &o. .
 ,~+O~:,:*,,O,...,:~~=**oox+:==~~~O=*x#&x    =..  
  ,.~~:,:.,.,.....,:,,~.,:~*~::~~===+Oo=     ,=.  
   ,..:~~:,,*:,....O,.~,,:~::::~:~?:,.~=     ~x.  
       :~:.,:,~xo~=x, ..,,,:,,~+=+~,~:+      ...  
    .,:?:?=:,:,,.=~::x.....+~+:,,::::=         .  
 :.....=~:,+:~,.:,:,.......?:=:,,~:==             
.: .* , :~....+.,:.~..,,.,.,.~=?O=:?      .  &&., 
         +~~.+=,,:...~.?.,,,,=,,~~~          ... ,
       ,.,,==,~,,+,...=+*+=*?=?=x*+ .        ,..  
   ,  .   .:,x:,=,:,....:,,:,:~:?,        ,:,=.. .
 :   .    ..,,.*#=,,.=,..~~+xoo+,,     .  =+      
,,.,.     ,.,~,..*O:,~::......+*                  
...        ..=,, ..:oo,~,,.~..=           .=..    
#            . . . .,:,,*###o             .. ~.   
  . ,           .* . .,.,.,~:~+:.                 
.            .   ,,  : .,  .. .?:~~~~:~~:,        
   ., ,  ,.        .~  . ::     ~~~#?,.  :=,      
~  . .  ,:  .    .  .  .,.~:  ::~,,*&..,::~,  .   
. , ,          o ?   . .,  :?,,,~~~,:      .      
:=.:~ ~**+,.     .     .     ..  .        ~       
```

# FALIZ 3.2 - EFFECT

Code name: **EFFECT**

_FALIZ is an elite asynchronous multi-agent AI for superdevs._

- Asyncio 5-queue orchestrator
- Personality: SASSY, ENTERPRISE, PRO TIPS
- Hotword + PyGame HUD
- Legal risk scoring, SecOps, memory persistence
- OpenAI, Claude, Gemini, Eleven Labs (all mixed!)

See `requirements.txt` for setup dependencies.

---

## 🚀 How To Deploy and Use FALIZ 3.2 AI

### 1. Deploy on PythonAnywhere (Web/Phone Friendly)

1. **Clone your repo:**
   ```bash
   git clone https://github.com/gamesiteonline/AI.git
   cd AI
   ```

2. **Create a PythonAnywhere virtual environment:**
   ```bash
   python3.10 -m venv venv
   source venv/bin/activate
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

3. **Set API Keys (in Bash console, and add to `.env` for persistence):**
   ```bash
   echo "OPENAI_API_KEY=your-openai-key" >> .env
   echo "ANTHROPIC_API_KEY=your-anthropic-key" >> .env
   echo "GEMINI_API_KEY=your-google-api-key" >> .env
   echo "ELEVENLABS_API_KEY=your-11labs-key" >> .env
   echo "TWILIO_SID=your-twilio-sid" >> .env
   echo "TWILIO_TOKEN=your-twilio-token" >> .env
   echo "TWILIO_FROM_NUMBER=+1xxxx" >> .env
   echo "FALIZ_ADMIN_EMAIL=fahadgroyne@gmail.com" >> .env
   echo "FALIZ_ADMIN_PASSWORD=@fahadmohamed" >> .env
   ```

4. **Port and GUI fix:**
   - Use port 8000 for web endpoints. PythonAnywhere does not allow GUI, so disable or comment out the PyGame HUD tasks in `main.py`.
   - Deploy using FastAPI (see code example in README).

5. **Open PythonAnywhere web dashboard, set up your web app to point to ASGI/WSGI file.**

---

### 2. Admin Email / Auth
- **Admin Email**: fahadgroyne@gmail.com  
- **Admin Password**: @fahadmohamed  
- _(Add to `.env` for security; don't hard-code to repo)_

---

### 3. Voice, Speech, and Telephony

- **Human-like TTS**: Provided in `modules/speech.py` (uses ElevenLabs).
- **Send SMS/Text**: Use `modules/telephony.py` (Twilio integration).
- **To generate speech:**
  ```python
  from modules.speech import SpeechSynthesizer, TextToSpeechRequest
  synth = SpeechSynthesizer()
  mp3_bytes = await synth.synthesize(TextToSpeechRequest(text="Hello! Welcome to FALIZ 3.2!"))
  # Serve as audio or save
  ```
- **To send SMS:**
  ```python
  from modules.telephony import Telephony, SMSRequest
  tel = Telephony()
  tel.send_sms(SMSRequest(to="+1234567890", body="Test from FALIZ!")) 
  ```

---

### 4. Troubleshooting for PythonAnywhere

- Use only port 8000 for HTTP endpoints.
- All secret credentials/API keys/passwords must be in `.env` or the environment variables setting in PAW.
- Disable PyGame HUD when running headless (web only).
- Audio input and GUI will not work on PAW web; use text endpoints.

---

### 5. Extend/Integrate

- Add new FastAPI endpoints for `/ai/chat`, `/ai/tts`, `/ai/sms` as shown.
- For mobile: wrap web interface as a PWA for best experience.

---

**All modules and integrations are now production-ready and PythonAnywhere/web-capable!**
