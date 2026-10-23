from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

quotes = [

    {"text": "Knowledge is power.", "author": "Francis Bacon"},
    {"text": "Well begun is half done.", "author": "Aristotle"},
    {"text": "Nothing will work unless you do.", "author": "Maya Angelou"},
    {"text": "The best way out is always through.", "author": "Robert Frost"},
    {"text": "No act of kindness, no matter how small, is ever wasted.", "author": "Aesop"},
    {"text": "To be, or not to be, that is the question.", "author": "William Shakespeare"},
    {"text": "Our doubts are traitors.", "author": "William Shakespeare"},
    {"text": "Fortune favors the bold.", "author": "Virgil"},
    {"text": "Nothing great was ever achieved without enthusiasm.", "author": "Ralph Waldo Emerson"},
    {"text": "Adopt the pace of nature: her secret is patience.", "author": "Ralph Waldo Emerson"},

    {"text": "The secret of education lies in respecting the pupil.", "author": "Ralph Waldo Emerson"},
    {"text": "The only way to have a friend is to be one.", "author": "Ralph Waldo Emerson"},
    {"text": "Do not go where the path may lead; go instead where there is no path.", "author": "Ralph Waldo Emerson"},
    {"text": "Energy and persistence conquer all things.", "author": "Benjamin Franklin"},
    {"text": "Well done is better than well said.", "author": "Benjamin Franklin"},
    {"text": "Lost time is never found again.", "author": "Benjamin Franklin"},
    {"text": "An investment in knowledge pays the best interest.", "author": "Benjamin Franklin"},
    {"text": "By failing to prepare, you are preparing to fail.", "author": "Benjamin Franklin"},
    {"text": "He that can have patience can have what he will.", "author": "Benjamin Franklin"},
    {"text": "Without continual growth and progress, such words as improvement, achievement, and success have no meaning.", "author": "Benjamin Franklin"},

    {"text": "The unexamined life is not worth living.", "author": "Socrates"},
    {"text": "The beginning is the most important part of the work.", "author": "Plato"},
    {"text": "Courage is knowing what not to fear.", "author": "Plato"},
    {"text": "The secret of change is to focus all of your energy, not on fighting the old, but on building the new.", "author": "Socrates"},
    {"text": "The journey of a thousand miles begins with a single step.", "author": "Lao Tzu"},
    {"text": "He who knows others is wise; he who knows himself is enlightened.", "author": "Lao Tzu"},
    {"text": "A good traveler has no fixed plans.", "author": "Lao Tzu"},
    {"text": "Nature does not hurry, yet everything is accomplished.", "author": "Lao Tzu"},
    {"text": "The superior man is modest in his speech, but exceeds in his actions.", "author": "Confucius"},
    {"text": "It does not matter how slowly you go as long as you do not stop.", "author": "Confucius"},

    {"text": "Real knowledge is to know the extent of one's ignorance.", "author": "Confucius"},
    {"text": "The man who moves a mountain begins by carrying away small stones.", "author": "Confucius"},
    {"text": "Everything has beauty, but not everyone sees it.", "author": "Confucius"},
    {"text": "Wherever you go, go with all your heart.", "author": "Confucius"},
    {"text": "Waste no more time arguing what a good man should be. Be one.", "author": "Marcus Aurelius"},
    {"text": "The happiness of your life depends upon the quality of your thoughts.", "author": "Marcus Aurelius"},
    {"text": "You have power over your mind—not outside events.", "author": "Marcus Aurelius"},
    {"text": "The impediment to action advances action.", "author": "Marcus Aurelius"},
    {"text": "Difficulties strengthen the mind, as labor does the body.", "author": "Seneca"},
    {"text": "Luck is what happens when preparation meets opportunity.", "author": "Seneca"},

    {"text": "We suffer more often in imagination than in reality.", "author": "Seneca"},
    {"text": "Begin at once to live, and count each separate day as a separate life.", "author": "Seneca"},
    {"text": "It is not that we have a short time to live, but that we waste a lot of it.", "author": "Seneca"},
    {"text": "While we teach, we learn.", "author": "Seneca"},
    {"text": "He who is brave is free.", "author": "Seneca"},
    {"text": "Nothing is so difficult that it cannot be overcome by diligence.", "author": "Terence"},
    {"text": "I am not afraid of storms, for I am learning how to sail my ship.", "author": "Louisa May Alcott"},
    {"text": "I have not failed. I've just found 10,000 ways that won't work.", "author": "Thomas Edison"},
    {"text": "Genius is one percent inspiration and ninety-nine percent perspiration.", "author": "Thomas Edison"},
    {"text": "Opportunity is missed by most people because it is dressed in overalls and looks like work.", "author": "Thomas Edison"},

    {"text": "Nothing is particularly hard if you divide it into small jobs.", "author": "Henry Ford"},
    {"text": "Whether you think you can, or you think you can't—you're right.", "author": "Henry Ford"},
    {"text": "Failure is simply the opportunity to begin again, this time more intelligently.", "author": "Henry Ford"},
    {"text": "Quality means doing it right when no one is looking.", "author": "Henry Ford"},
    {"text": "It always seems impossible until it's done.", "author": "Nelson Mandela"},
    {"text": "Education is the most powerful weapon which you can use to change the world.", "author": "Nelson Mandela"},
    {"text": "After climbing a great hill, one only finds that there are many more hills to climb.", "author": "Nelson Mandela"},
    {"text": "The greatest glory in living lies not in never falling, but in rising every time we fall.", "author": "Nelson Mandela"},
    {"text": "If there is no struggle, there is no progress.", "author": "Frederick Douglass"},
    {"text": "It is easier to build strong children than to repair broken men.", "author": "Frederick Douglass"},

    {"text": "The future belongs to those who believe in the beauty of their dreams.", "author": "Eleanor Roosevelt"},
    {"text": "No one can make you feel inferior without your consent.", "author": "Eleanor Roosevelt"},
    {"text": "You must do the thing you think you cannot do.", "author": "Eleanor Roosevelt"},
    {"text": "The purpose of life is to live it, to taste experience to the utmost.", "author": "Eleanor Roosevelt"},
    {"text": "Keep your face always toward the sunshine—and shadows will fall behind you.", "author": "Walt Whitman"},
    {"text": "Do anything, but let it produce joy.", "author": "Walt Whitman"},
    {"text": "I exist as I am, that is enough.", "author": "Walt Whitman"},
    {"text": "The powerful play goes on, and you may contribute a verse.", "author": "Walt Whitman"},
    {"text": "Hope is the thing with feathers.", "author": "Emily Dickinson"},
    {"text": "Forever is composed of nows.", "author": "Emily Dickinson"},

    {"text": "We never know how high we are till we are called to rise.", "author": "Emily Dickinson"},
    {"text": "There is no greater agony than bearing an untold story inside you.", "author": "Maya Angelou"},
    {"text": "Nothing can dim the light that shines from within.", "author": "Maya Angelou"},
    {"text": "Try to be a rainbow in someone's cloud.", "author": "Maya Angelou"},
    {"text": "You may encounter many defeats, but you must not be defeated.", "author": "Maya Angelou"},
    {"text": "Life is either a daring adventure or nothing.", "author": "Helen Keller"},
    {"text": "Alone we can do so little; together we can do so much.", "author": "Helen Keller"},
    {"text": "Keep your face to the sunshine and you cannot see a shadow.", "author": "Helen Keller"},
    {"text": "The most beautiful things in the world cannot be seen or even touched.", "author": "Helen Keller"},
    {"text": "Optimism is the faith that leads to achievement.", "author": "Helen Keller"},

    {"text": "A person who never made a mistake never tried anything new.", "author": "Albert Einstein"},
    {"text": "Imagination is more important than knowledge.", "author": "Albert Einstein"},
    {"text": "Learn from yesterday, live for today, hope for tomorrow.", "author": "Albert Einstein"},
    {"text": "Life is like riding a bicycle. To keep your balance, you must keep moving.", "author": "Albert Einstein"},
    {"text": "Try not to become a person of success, but rather try to become a person of value.", "author": "Albert Einstein"},
    {"text": "The important thing is not to stop questioning.", "author": "Albert Einstein"},
    {"text": "Strive not to be a success, but rather to be of value.", "author": "Albert Einstein"},
    {"text": "The secret of getting ahead is getting started.", "author": "Mark Twain"},
    {"text": "The man who does not read has no advantage over the man who cannot read.", "author": "Mark Twain"},
    {"text": "Kindness is the language which the deaf can hear and the blind can see.", "author": "Mark Twain"},

    {"text": "Courage is resistance to fear, mastery of fear—not absence of fear.", "author": "Mark Twain"},
    {"text": "The two most important days in your life are the day you are born and the day you find out why.", "author": "Mark Twain"},
    {"text": "Act as if what you do makes a difference. It does.", "author": "William James"},
    {"text": "The greatest weapon against stress is our ability to choose one thought over another.", "author": "William James"},
    {"text": "Believe that life is worth living and your belief will help create the fact.", "author": "William James"},
    {"text": "Nothing is worth more than this day.", "author": "Johann Wolfgang von Goethe"},
    {"text": "Knowing is not enough; we must apply. Willing is not enough; we must do.", "author": "Johann Wolfgang von Goethe"},
    {"text": "Whatever you can do, or dream you can, begin it.", "author": "Johann Wolfgang von Goethe"},
    {"text": "A man sees in the world what he carries in his heart.", "author": "Johann Wolfgang von Goethe"},
    {"text": "The soul that sees beauty may sometimes walk alone.", "author": "Johann Wolfgang von Goethe"},

    # Dr. A.P.J. Abdul Kalam
    {"text": "Dream, dream, dream. Dreams transform into thoughts and thoughts result in action.", "author": "A.P.J. Abdul Kalam"},
    {"text": "Thinking is progress. Thinking leads to action.", "author": "A.P.J. Abdul Kalam"},
    {"text": "Knowledge without action is useless and irrelevant.", "author": "A.P.J. Abdul Kalam"},
    {"text": "Thinking should become your capital asset.", "author": "A.P.J. Abdul Kalam"},
    {"text": "Small aim is a crime.", "author": "A.P.J. Abdul Kalam"},
    {"text": "The ignited mind of the youth is the most powerful resource on the earth.", "author": "A.P.J. Abdul Kalam"},
    {"text": "To succeed in your mission, you must have single-minded devotion to your goal.", "author": "A.P.J. Abdul Kalam"},
    {"text": "Excellence is a continuous process and not an accident.", "author": "A.P.J. Abdul Kalam"},
    {"text": "We should not give up and we should not allow the problem to defeat us.", "author": "A.P.J. Abdul Kalam"},
    {"text": "Let us sacrifice our today so that our children can have a better tomorrow.", "author": "A.P.J. Abdul Kalam"},

    # Swami Vivekananda
    {"text": "Arise, awake, and stop not till the goal is reached.", "author": "Swami Vivekananda"},
    {"text": "Take up one idea. Make that one idea your life.", "author": "Swami Vivekananda"},
    {"text": "Strength is life, weakness is death.", "author": "Swami Vivekananda"},
    {"text": "The remedy for weakness is not brooding over weakness, but thinking of strength.", "author": "Swami Vivekananda"},
    {"text": "You cannot believe in God until you believe in yourself.", "author": "Swami Vivekananda"},
    {"text": "In a conflict between the heart and the brain, follow your heart.", "author": "Swami Vivekananda"},
    {"text": "All power is within you; you can do anything and everything.", "author": "Swami Vivekananda"},
    {"text": "Purity, patience, and perseverance are the three essentials to success.", "author": "Swami Vivekananda"},
    {"text": "The world is the great gymnasium where we come to make ourselves strong.", "author": "Swami Vivekananda"},
    {"text": "They alone live who live for others.", "author": "Swami Vivekananda"},

    # Mahatma Gandhi
    {"text": "The future depends on what you do today.", "author": "Mahatma Gandhi"},
    {"text": "In a gentle way, you can shake the world.", "author": "Mahatma Gandhi"},
    {"text": "The best way to find yourself is to lose yourself in the service of others.", "author": "Mahatma Gandhi"},
    {"text": "Strength does not come from physical capacity. It comes from an indomitable will.", "author": "Mahatma Gandhi"},
    {"text": "An ounce of practice is worth more than tons of preaching.", "author": "Mahatma Gandhi"},
    {"text": "Happiness is when what you think, what you say, and what you do are in harmony.", "author": "Mahatma Gandhi"},
    {"text": "The good man is the friend of all living things.", "author": "Mahatma Gandhi"},
    {"text": "Truth never damages a cause that is just.", "author": "Mahatma Gandhi"},
    {"text": "A man is but the product of his thoughts.", "author": "Mahatma Gandhi"},
    {"text": "The difference between what we do and what we are capable of doing would suffice to solve most of the world's problems.", "author": "Mahatma Gandhi"},

    # Dr. B. R. Ambedkar
    {"text": "Life should be great rather than long.", "author": "B. R. Ambedkar"},
    {"text": "Cultivation of mind should be the ultimate aim of human existence.", "author": "B. R. Ambedkar"},
    {"text": "We are Indians, firstly and lastly.", "author": "B. R. Ambedkar"},
    {"text": "Be educated, be organised, and be agitated.", "author": "B. R. Ambedkar"},
    {"text": "I measure the progress of a community by the degree of progress which women have achieved.", "author": "B. R. Ambedkar"},
    {"text": "Freedom of mind is the real freedom.", "author": "B. R. Ambedkar"},
    {"text": "A great man is different from an eminent one in that he is ready to be the servant of society.", "author": "B. R. Ambedkar"},
    {"text": "Political democracy cannot last unless there lies at the base of it social democracy.", "author": "B. R. Ambedkar"},
    {"text": "Equality may be a fiction but nonetheless one must accept it as a governing principle.", "author": "B. R. Ambedkar"},
    {"text": "So long as you do not achieve social liberty, whatever freedom is provided by the law is of no avail to you.", "author": "B. R. Ambedkar"},

    # Rabindranath Tagore
    {"text": "You can't cross the sea merely by standing and staring at the water.", "author": "Rabindranath Tagore"},
    {"text": "Faith is the bird that feels the light when the dawn is still dark.", "author": "Rabindranath Tagore"},
    {"text": "Let your life lightly dance on the edges of Time like dew on the tip of a leaf.", "author": "Rabindranath Tagore"},
    {"text": "The butterfly counts not months but moments, and has time enough.", "author": "Rabindranath Tagore"},
    {"text": "Where the mind is without fear and the head is held high.", "author": "Rabindranath Tagore"},
    {"text": "The highest education is that which does not merely give us information but makes our life in harmony with all existence.", "author": "Rabindranath Tagore"},
    {"text": "Everything comes to us that belongs to us if we create the capacity to receive it.", "author": "Rabindranath Tagore"},
    {"text": "Don't limit a child to your own learning, for they were born in another time.", "author": "Rabindranath Tagore"},
    {"text": "Love does not claim possession, but gives freedom.", "author": "Rabindranath Tagore"},
    {"text": "The roots below the earth claim no rewards for making the branches fruitful.", "author": "Rabindranath Tagore"},

    # Netaji Subhas Chandra Bose
    {"text": "Give me blood, and I shall give you freedom.", "author": "Subhas Chandra Bose"},
    {"text": "Freedom is not given, it is taken.", "author": "Subhas Chandra Bose"},
    {"text": "Life loses half its interest if there is no struggle.", "author": "Subhas Chandra Bose"},
    {"text": "It is blood alone that can pay the price of freedom.", "author": "Subhas Chandra Bose"},
    {"text": "No real change in history has ever been achieved by discussions.", "author": "Subhas Chandra Bose"},

    # Jawaharlal Nehru
    {"text": "The only alternative to coexistence is co-destruction.", "author": "Jawaharlal Nehru"},
    {"text": "Facts are facts and will not disappear on account of your likes.", "author": "Jawaharlal Nehru"},
    {"text": "A moment comes, which comes but rarely in history, when we step out from the old to the new.", "author": "Jawaharlal Nehru"},
    {"text": "Ignorance is always afraid of change.", "author": "Jawaharlal Nehru"},
    {"text": "Culture is the widening of the mind and of the spirit.", "author": "Jawaharlal Nehru"},

    # Sardar Vallabhbhai Patel
    {"text": "Manpower without unity is not a strength unless it is harmonised and united properly.", "author": "Sardar Vallabhbhai Patel"},
    {"text": "Take to the path of dharma—the path of truth and justice.", "author": "Sardar Vallabhbhai Patel"},
    {"text": "Faith is of no avail in the absence of strength.", "author": "Sardar Vallabhbhai Patel"},
    {"text": "Every citizen of India must remember that he is an Indian and he has every right in this country but with certain duties.", "author": "Sardar Vallabhbhai Patel"},
    {"text": "There is something unique in this soil, which despite many obstacles has always remained the abode of great souls.", "author": "Sardar Vallabhbhai Patel"},

    # Bhagat Singh
    {"text": "Merciless criticism and independent thinking are the two necessary traits of revolutionary thinking.", "author": "Bhagat Singh"},
    {"text": "Revolution is an inalienable right of mankind.", "author": "Bhagat Singh"},
    {"text": "The aim of life is no more to control the mind, but to develop it harmoniously.", "author": "Bhagat Singh"},
    {"text": "Any man who stands for progress has to criticize, disbelieve and challenge every item of the old faith.", "author": "Bhagat Singh"},
    {"text": "Bombs and pistols do not make a revolution.", "author": "Bhagat Singh"},

    # Sarojini Naidu
    {"text": "We want deeper sincerity of motive, a greater courage in speech, and earnestness in action.", "author": "Sarojini Naidu"},
    {"text": "A country's greatness lies in its undying ideals of love and sacrifice.", "author": "Sarojini Naidu"},
    {"text": "When there is oppression, the only self-respecting thing is to rise and say this shall cease today.", "author": "Sarojini Naidu"},
    {"text": "We must break down the barriers between us and the rest of the world.", "author": "Sarojini Naidu"},
    {"text": "A nation's culture resides in the hearts and in the soul of its people.", "author": "Mahatma Gandhi"},

    # Chanakya
    {"text": "Education is the best friend. An educated person is respected everywhere.", "author": "Chanakya"},
    {"text": "Before you start some work, always ask yourself three questions: why, what, and how.", "author": "Chanakya"},
    {"text": "Once you start a work, do not be afraid of failure and do not abandon it.", "author": "Chanakya"},
    {"text": "The fragrance of flowers spreads only in the direction of the wind, but the goodness of a person spreads in all directions.", "author": "Chanakya"},
    {"text": "A person should not be too honest. Straight trees are cut first.", "author": "Chanakya"},

    # Tiruvalluvar
    {"text": "The wound caused by fire heals; the wound caused by the tongue never heals.", "author": "Tiruvalluvar"},
    {"text": "Learning is excellence that none can destroy.", "author": "Tiruvalluvar"},
    {"text": "The world belongs to those who act with diligence.", "author": "Tiruvalluvar"},
    {"text": "Virtue yields honour and prosperity.", "author": "Tiruvalluvar"},
    {"text": "The wealth of the wise is the wealth of kindness.", "author": "Tiruvalluvar"},

    # Other Indian thinkers and leaders
    {"text": "A country's greatness lies in its undying ideals of love and sacrifice.", "author": "Sarojini Naidu"},
    {"text": "The best way to predict the future is to create it.", "author": "Dr. A. P. J. Abdul Kalam"},
    {"text": "Where there is righteousness in the heart, there is beauty in the character.", "author": "A. P. J. Abdul Kalam"},
    {"text": "Be the change that you wish to see in the world.", "author": "Mahatma Gandhi"},
    {"text": "Swaraj is my birthright and I shall have it.", "author": "Bal Gangadhar Tilak"},
    {"text": "Self-confidence and self-reliance are the main ingredients of a successful life.", "author": "Swami Vivekananda"},
    {"text": "A nation's culture resides in the hearts and in the soul of its people.", "author": "Mahatma Gandhi"},
    {"text": "The true teachers are those who help us think for ourselves.", "author": "Dr. Sarvepalli Radhakrishnan"},
    {"text": "The end-product of education should be a free creative man.", "author": "Dr. Sarvepalli Radhakrishnan"},
    {"text": "Dreams are not those which come while we are sleeping, but dreams are those when you don't sleep before fulfilling them.", "author": "A. P. J. Abdul Kalam"}
]
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/quote")
def get_quote():
    return jsonify(random.choice(quotes))

@app.route("/api/quotes")
def get_quotes():
    return jsonify(quotes)

if __name__ == "__main__":
    app.run(debug=True)