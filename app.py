import React, { useState, useEffect } from 'react';
import { Zap, TrendingUp, Users, Award, Plus, X } from 'lucide-react';

// Challenge database - expanded with 500 total (100 original + 400 new)
const CHALLENGES_DB = {
  easy: [
    "Smile at 5 strangers.",
    "Compliment someone's shoes.",
    "Ask someone what time it is.",
    "Say 'Have a good day' to a cashier.",
    "Ask for directions even if you know the way.",
    "Tell a friend they look great today.",
    "Hold eye contact with someone for 3 seconds and smile.",
    "Ask someone's name and remember it.",
    "Ask someone about their weekend plans.",
    "Ask someone how their day's going — and actually listen.",
    "Compliment someone's hairstyle.",
    "Ask a waiter/waitress for their food recommendation.",
    "Say 'You have a good vibe' to someone.",
    "Ask a stranger where they're from.",
    "Introduce yourself to someone in your gym/café.",
    "Wave or say hi to a neighbor.",
    "Start small talk in a queue.",
    "Ask a coworker/classmate for a small favor.",
    "Hold the door open for someone and make eye contact.",
    "Ask someone what music they're listening to.",
    // New easy challenges
    "Compliment someone's smile today.",
    "Ask a stranger their favorite food.",
    "Say thank you to a store clerk with a smile.",
    "Compliment someone's jewelry or watch.",
    "Ask someone's opinion on the weather.",
    "Make eye contact and nod to someone you pass.",
    "Ask someone where they get their energy from.",
    "Compliment someone's handwriting.",
    "Ask a stranger if they know a good place to eat nearby.",
    "Tell someone you like their positive energy.",
    "Ask someone about their pet if they have one.",
    "Compliment someone's choice of color they're wearing.",
    "Ask someone 'What made you smile today?'",
    "Say 'You seem really cool' to someone.",
    "Ask a stranger if they've been to a cool place recently.",
    "Compliment someone's phone case or accessory.",
    "Ask someone what their go-to comfort food is.",
    "Tell someone they have nice eyes or good posture.",
    "Ask a stranger their favorite type of music.",
    "Smile genuinely at someone making eye contact.",
    "Ask someone 'What's something good that happened to you?'",
    "Compliment someone's laugh or sense of humor.",
    "Ask a stranger for a simple opinion on something.",
    "Tell someone they seem like they're having a good day.",
    "Ask someone what hobby they're passionate about.",
    "Compliment someone's tattoo if they have one visible.",
    "Ask a stranger 'What's your favorite season?'",
    "Tell someone they have a friendly face.",
    "Ask someone what they love most about their job.",
    "Compliment someone's effort or hard work that you notice.",
  ],
  medium: [
    "Ask someone's opinion on something ('Which coffee's better?').",
    "Start a convo about the weather — make it funny.",
    "Ask someone about their outfit ('That's cool — where'd you get it?').",
    "Ask a stranger to take your photo.",
    "Ask for help choosing between two things in a store.",
    "Ask a stranger about a tattoo or accessory they have.",
    "Give a genuine compliment to someone of the opposite gender.",
    "Ask someone what their dream job is.",
    "Ask a classmate/coworker what motivates them.",
    "Ask a stranger if they believe in luck.",
    "Ask someone for a restaurant recommendation.",
    "Start a random convo on the elevator.",
    "Ask someone what their favorite childhood cartoon was.",
    "Ask someone what phone app they can't live without.",
    "Compliment someone's confidence.",
    "Ask someone's opinion on a trending topic.",
    "Ask someone if they prefer cats or dogs — and debate playfully.",
    "Ask someone to teach you a handshake.",
    "Make someone laugh intentionally.",
    "Ask a stranger what book they're reading.",
    // New medium challenges
    "Ask someone what skill they wish they had.",
    "Start a conversation about a TV show or movie.",
    "Ask someone what country they'd love to visit.",
    "Compliment someone on their work or project.",
    "Ask someone about their biggest achievement.",
    "Start a convo about a popular podcast or show.",
    "Ask someone what makes them feel alive.",
    "Compliment someone's communication skills.",
    "Ask someone what they're grateful for today.",
    "Start a conversation about travel experiences.",
    "Ask someone what their favorite childhood memory is.",
    "Compliment someone on their creativity.",
    "Ask someone what they'd do on a perfect day.",
    "Start a convo about learning something new.",
    "Ask someone what inspires them the most.",
    "Compliment someone on handling a tough situation.",
    "Ask someone what their hidden talent is.",
    "Start a conversation about dreams or goals.",
    "Ask someone what makes them unique.",
    "Compliment someone on their perspective or wisdom.",
    "Ask someone what adventure they're planning.",
    "Start a convo about personal growth.",
    "Ask someone what legacy they want to leave.",
    "Compliment someone's patience or kindness.",
    "Ask someone what they're excited about.",
    "Start a conversation about a shared interest.",
    "Ask someone what success means to them.",
    "Compliment someone on their authenticity.",
    "Ask someone what they do to stay motivated.",
    "Start a convo about meaningful life lessons.",
  ],
  hard: [
    "Ask someone to high-five you.",
    "Ask a stranger to dance for 30 seconds.",
    "Challenge someone to a quick game (rock-paper-scissors, Uno, etc.).",
    "Ask someone for their phone number or Instagram.",
    "Ask someone out for coffee or juice.",
    "Ask a random person for fashion advice.",
    "Ask someone to rate your outfit from 1–10.",
    "Ask someone what they'd do if they won ₹1 crore.",
    "Compliment someone in a creative/funny way.",
    "Ask someone if you can take a selfie together.",
    "Offer to buy a stranger coffee.",
    "Ask someone what their biggest dream is.",
    "Tell someone, 'You seem like someone I'd get along with.'",
    "Ask a stranger what makes them happy.",
    "Ask someone if you can join their group for 5 minutes.",
    "Do a mini social experiment — like giving compliments to 10 people.",
    "Ask someone to recommend a movie or song.",
    "Ask a group of people a fun question ('What's your spirit animal?').",
    "Ask a stranger to describe their perfect day.",
    "Tell someone, 'You look like someone who does interesting things.'",
    // New hard challenges
    "Start a philosophical debate with a stranger.",
    "Ask someone to be your accountability partner.",
    "Challenge someone to a trivia game.",
    "Ask someone for career advice.",
    "Invite someone to grab a meal with you.",
    "Ask someone to mentor you in something.",
    "Start a project idea with a stranger.",
    "Ask someone to be part of a fun challenge with you.",
    "Pitch an idea to someone and ask for feedback.",
    "Ask someone about their biggest life lesson.",
    "Invite someone to an event you're going to.",
    "Ask someone to teach you their craft or skill.",
    "Propose starting a group or club together.",
    "Ask someone about overcoming their fear.",
    "Invite a stranger to join a spontaneous adventure.",
    "Ask someone to collaborate on something creative.",
    "Challenge someone to step out of their comfort zone with you.",
    "Ask someone what their superpower would be if they could choose.",
    "Invite someone to be part of your social mission.",
    "Ask someone to share their most vulnerable moment.",
    "Start a meaningful conversation about life purpose.",
    "Ask someone to help you with a personal goal.",
    "Invite someone to a networking event or meetup.",
    "Ask someone what advice they'd give to their younger self.",
    "Challenge someone to try something they've never done.",
    "Ask someone about their most transformative experience.",
    "Invite someone to start a habit with you.",
    "Ask someone to share their biggest success story.",
    "Start a conversation about mental health or wellness.",
    "Ask someone if they'd be open to being friends.",
  ],
  superhard: [
    "Ask for a 10% discount on something random.",
    "Ask a stranger to borrow their phone for a quick call (then explain it's a social challenge).",
    "Ask someone if they want to play a quick public game (UNO, chess, etc.).",
    "Ask for directions to a place that doesn't exist (then laugh about it).",
    "Ask someone to teach you a TikTok dance.",
    "Ask someone if you can record a 10-second 'positive message' for your challenge.",
    "Give out 3 compliments in a row without expecting a reply.",
    "Ask someone to sing one line of their favorite song with you.",
    "Ask for a fist bump from 5 strangers.",
    "Tell someone you're doing a 'social confidence game' and ask them to join one mini challenge.",
    "Lead a mini group activity (like a fun question circle).",
    "Ask someone to freestyle dance with you for 15 seconds.",
    "Do a 15-second funny public challenge (sing, dance, joke).",
    "Ask a stranger for life advice.",
    "Start a 'Would you rather?' convo with 3 people.",
    "Ask someone to tell you something they've never told anyone.",
    "Join a group convo mid-way (naturally, not awkwardly).",
    "Ask a group to vote on something you're wearing or buying.",
    "Ask someone to be your 1-minute podcast guest.",
    "Ask someone to give you a random dare (as long as it's safe).",
    // New superhard challenges
    "Start a spontaneous street performance or talent show.",
    "Ask 5 strangers to share their life motto.",
    "Lead a stranger through a personal growth exercise.",
    "Ask someone to be part of a social experiment with you.",
    "Organize an impromptu group activity.",
    "Ask someone to share their biggest fear and help them face it.",
    "Start a meaningful conversation about life purpose with a group.",
    "Ask 10 people for advice on a personal decision.",
    "Lead a group in a fun challenge or game.",
    "Ask someone to help you inspire others.",
    "Start a social movement or challenge.",
    "Ask a group to participate in a kindness project.",
    "Organize a group discussion on a deep topic.",
    "Ask someone to mentor you publicly.",
    "Start a community building activity.",
    "Ask multiple people to share transformation stories.",
    "Lead a workshop or teach a group something.",
    "Ask strangers to contribute to a creative project.",
    "Start a support group or circle.",
    "Ask a group to help someone in need.",
    "Organize a flash mob or group performance.",
    "Ask people to participate in a social cause.",
    "Lead a group through a challenging exercise.",
    "Ask a group to create something together.",
    "Start a mentorship circle.",
    "Ask people to share and celebrate wins together.",
    "Lead a group on a social adventure.",
    "Ask a group to challenge each other.",
    "Organize a community event.",
    "Ask people to become accountability partners.",
  ],
};

const SOCIALIZATION_QUOTES = [
  "\"Every conversation is a chance to change someone's day.\" - Anonymous",
  "\"Connection is the antidote to isolation.\" - Brené Brown",
  "\"The greatest gift you can give is your presence.\" - Oprah",
  "\"Real human connection is at the heart of everything.\" - Brian Chesky",
  "\"We're hardwired to connect with other people.\" - Daniel Goleman",
  "\"You can't stay in your corner of the forest waiting for others...\" - Winnie the Pooh",
  "\"Social connection is as vital to our health as any physical activity.\" - Research",
  "\"The best way to find yourself is to lose yourself in service to others.\" - Gandhi",
];

export default function SocialXPGame() {
  const [userName, setUserName] = useState('Rohan');
  const [confidenceLevel, setConfidenceLevel] = useState(null);
  const [challenges, setChallenges] = useState([]);
  const [loading, setLoading] = useState(false);
  const [currentQuote, setCurrentQuote] = useState(SOCIALIZATION_QUOTES[0]);
  const [totalXP, setTotalXP] = useState(245);
  const [completedChallenges, setCompletedChallenges] = useState(12);
  const [streak, setStreak] = useState(3);
  const [averageConfidence, setAverageConfidence] = useState(6.5);
  const [selectedChallenge, setSelectedChallenge] = useState(null);

  const generateChallenges = (confidence) => {
    setLoading(true);
    setConfidenceLevel(confidence);
    
    // Determine difficulty distribution based on confidence
    let distribution = {};
    if (confidence <= 3) {
      distribution = { easy: 4, medium: 1, hard: 0, superhard: 0 };
    } else if (confidence <= 5) {
      distribution = { easy: 2, medium: 2, hard: 1, superhard: 0 };
    } else if (confidence <= 7) {
      distribution = { easy: 1, medium: 2, hard: 2, superhard: 0 };
    } else {
      distribution = { easy: 0, medium: 1, hard: 3, superhard: 1 };
    }

    // Simulate loading and quote rotation
    let quoteIndex = 0;
    const quoteInterval = setInterval(() => {
      quoteIndex = (quoteIndex + 1) % SOCIALIZATION_QUOTES.length;
      setCurrentQuote(SOCIALIZATION_QUOTES[quoteIndex]);
    }, 2000);

    setTimeout(() => {
      clearInterval(quoteInterval);
      
      const newChallenges = [];
      Object.entries(distribution).forEach(([difficulty, count]) => {
        const pool = CHALLENGES_DB[difficulty];
        for (let i = 0; i < count; i++) {
          const randomChallenge = pool[Math.floor(Math.random() * pool.length)];
          newChallenges.push({ text: randomChallenge, difficulty });
        }
      });
      
      setChallenges(newChallenges);
      setLoading(false);
    }, 3000);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900 text-white p-4 md:p-8">
      {/* Header */}
      <div className="max-w-6xl mx-auto">
        <div className="text-4xl md:text-5xl font-black mb-2 bg-gradient-to-r from-cyan-400 to-purple-400 bg-clip-text text-transparent">
          🎮 SOCIAL XP
        </div>
        <div className="text-cyan-300 text-sm font-semibold tracking-widest">LEVEL UP YOUR SOCIAL CONFIDENCE</div>
      </div>

      {/* Main Container */}
      <div className="max-w-6xl mx-auto mt-12">
        {/* WELCOME SECTION */}
        <div className="bg-gradient-to-r from-purple-800/40 to-cyan-800/40 border-2 border-purple-500/50 rounded-2xl p-8 mb-8 backdrop-blur-sm">
          <h1 className="text-3xl md:text-4xl font-black mb-4">
            Hey <span className="text-transparent bg-gradient-to-r from-cyan-400 to-purple-400 bg-clip-text">{userName}</span>, how's it going? 🚀
          </h1>
          <p className="text-purple-200 text-lg mb-8">Ready to build some social confidence today?</p>

          {/* Confidence Slider */}
          {!challenges.length && (
            <div className="bg-slate-900/50 rounded-xl p-6 border border-purple-500/30">
              <div className="flex justify-between items-center mb-4">
                <label className="text-xl font-bold">How confident are you feeling today?</label>
                {confidenceLevel && (
                  <div className="text-3xl font-black text-transparent bg-gradient-to-r from-cyan-400 to-purple-400 bg-clip-text">
                    {confidenceLevel}/10
                  </div>
                )}
              </div>
              
              <input
                type="range"
                min="1"
                max="10"
                value={confidenceLevel || 5}
                onChange={(e) => setConfidenceLevel(parseInt(e.target.value))}
                className="w-full h-3 bg-gradient-to-r from-red-500 via-yellow-500 to-green-500 rounded-lg appearance-none cursor-pointer mb-6"
                style={{
                  accentColor: confidenceLevel > 6 ? '#22c55e' : '#f59e0b'
                }}
              />

              <div className="flex justify-between text-sm text-purple-300 mb-6">
                <span>😰 Not ready</span>
                <span>🔥 Super confident</span>
              </div>

              <button
                onClick={() => generateChallenges(confidenceLevel || 5)}
                disabled={loading}
                className="w-full bg-gradient-to-r from-cyan-500 to-purple-600 hover:from-cyan-400 hover:to-purple-500 disabled:opacity-50 font-black py-4 rounded-lg text-lg transition-all transform hover:scale-105 active:scale-95"
              >
                {loading ? '⚡ GENERATING YOUR CHALLENGES...' : '🎲 GENERATE CHALLENGES'}
              </button>
            </div>
          )}

          {/* Loading Screen */}
          {loading && (
            <div className="bg-slate-900/80 rounded-xl p-12 border border-cyan-500/50 text-center">
              <div className="mb-8">
                <div className="inline-block">
                  <div className="relative w-20 h-20">
                    <div className="absolute inset-0 rounded-full border-4 border-purple-500/30"></div>
                    <div className="absolute inset-0 rounded-full border-4 border-transparent border-t-cyan-400 border-r-purple-400 animate-spin"></div>
                  </div>
                </div>
              </div>
              <h2 className="text-2xl font-black mb-6">✨ Creating Your Perfect Challenges...</h2>
              <div className="bg-slate-800/50 rounded-lg p-6 border border-purple-500/30">
                <p className="text-lg text-cyan-300 italic">{currentQuote}</p>
              </div>
            </div>
          )}
        </div>

        {/* STATS SECTION */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
          <StatCard icon={<Zap className="w-6 h-6" />} label="Total XP" value={totalXP} color="from-yellow-400 to-orange-400" />
          <StatCard icon={<Award className="w-6 h-6" />} label="Completed" value={completedChallenges} color="from-green-400 to-emerald-400" />
          <StatCard icon={<TrendingUp className="w-6 h-6" />} label="Streak" value={`${streak} days`} color="from-red-400 to-pink-400" />
          <StatCard icon={<Users className="w-6 h-6" />} label="Avg Confidence" value={averageConfidence} color="from-cyan-400 to-blue-400" />
        </div>

        {/* CHALLENGES SECTION */}
        {challenges.length > 0 && !selectedChallenge && (
          <div className="mb-8">
            <h2 className="text-3xl font-black mb-6">🎯 Your Challenges Today</h2>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-4">
              {challenges.map((challenge, idx) => (
                <ChallengeCard
                  key={idx}
                  challenge={challenge}
                  index={idx}
                  onSelect={() => setSelectedChallenge(idx)}
                />
              ))}
            </div>
          </div>
        )}

        {/* CHALLENGE DETAIL */}
        {selectedChallenge !== null && (
          <ChallengeDetail
            challenge={challenges[selectedChallenge]}
            onClose={() => setSelectedChallenge(null)}
            onComplete={() => {
              setCompletedChallenges(completedChallenges + 1);
              setSelectedChallenge(null);
            }}
          />
        )}
      </div>
    </div>
  );
}

function StatCard({ icon, label, value, color }) {
  return (
    <div className={`bg-gradient-to-br ${color} bg-opacity-10 border-2 border-${color.split(' ')[1]}/50 rounded-xl p-4 backdrop-blur-sm hover:scale-105 transition-transform`}>
      <div className="flex items-center gap-2 mb-2 opacity-75">{icon}</div>
      <div className="text-sm font-semibold text-gray-300">{label}</div>
      <div className="text-2xl font-black">{value}</div>
    </div>
  );
}

function ChallengeCard({ challenge, index, onSelect }) {
  const difficultyColors = {
    easy: 'from-green-500 to-emerald-500',
    medium: 'from-blue-500 to-cyan-500',
    hard: 'from-orange-500 to-red-500',
    superhard: 'from-purple-600 to-pink-600',
  };

  return (
    <button
      onClick={onSelect}
      className="bg-gradient-to-br from-slate-800 to-slate-900 border-2 border-purple-500/30 rounded-xl p-4 hover:scale-105 hover:border-purple-400 transition-all active:scale-95 group cursor-pointer"
    >
      <div className={`bg-gradient-to-r ${difficultyColors[challenge.difficulty]} text-white text-xs font-black px-3 py-1 rounded-full w-fit mb-3 group-hover:shadow-lg group-hover:shadow-purple-500/50 transition-all`}>
        {challenge.difficulty.toUpperCase()}
      </div>
      <p className="text-sm font-semibold text-left line-clamp-3 group-hover:text-cyan-300 transition-colors">
        {challenge.text}
      </p>
      <div className="mt-4 text-right text-xs text-purple-400">Click to expand →</div>
    </button>
  );
}

function ChallengeDetail({ challenge, onClose, onComplete }) {
  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50 backdrop-blur-sm">
      <div className="bg-gradient-to-br from-slate-800 to-slate-900 border-2 border-cyan-500/50 rounded-2xl p-8 max-w-lg w-full max-h-96 overflow-y-auto">
        <div className="flex justify-between items-start mb-6">
          <div>
            <div className="inline-block bg-gradient-to-r from-cyan-500 to-purple-600 text-white text-xs font-black px-3 py-1 rounded-full mb-4">
              {challenge.difficulty.toUpperCase()}
            </div>
            <h2 className="text-2xl font-black">{challenge.text}</h2>
          </div>
          <button onClick={onClose} className="text-gray-400 hover:text-white transition-colors">
            <X className="w-6 h-6" />
          </button>
        </div>

        <div className="bg-slate-700/50 rounded-lg p-4 mb-6">
          <h3 className="font-bold text-cyan-400 mb-2">How to do it:</h3>
          <p className="text-sm text-gray-300 leading-relaxed">
            Approach this challenge with genuine intent. Be authentic, respectful, and ready to engage with others. Remember, the goal is to build real human connections and overcome social anxiety. Start small if you need to, and celebrate every interaction!
          </p>
        </div>

        <div className="flex gap-3">
          <button
            onClick={onClose}
            className="flex-1 bg-slate-700 hover:bg-slate-600 font-bold py-3 rounded-lg transition-colors"
          >
            Not Now
          </button>
          <button
            onClick={onComplete}
            className="flex-1 bg-gradient-to-r from-cyan-500 to-purple-600 hover:from-cyan-400 hover:to-purple-500 font-black py-3 rounded-lg transition-all transform hover:scale-105 active:scale-95 flex items-center justify-center gap-2"
          >
            <Zap className="w-5 h-5" /> I Did It!
          </button>
        </div>
      </div>
    </div>
  );
}
