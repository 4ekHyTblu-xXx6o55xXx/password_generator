LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"
SPECIAL = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

# Без неоднозначных символов (l, I, 1, 0, O)
UNAMBIGUOUS_LOWERCASE = "abcdefghijkmnopqrstuvwxyz"      # без l
UNAMBIGUOUS_UPPERCASE = "ABCDEFGHJKLMNPQRSTUVWXYZ"      # без I, O
UNAMBIGUOUS_DIGITS = "23456789"                         # без 0,1
UNAMBIGUOUS_SPECIAL = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

# Список слов для генерации фраз
WORD_LIST = [
    # Исходные слова (сохранены)
    "apple", "orange", "banana", "grape", "kiwi", "peach", "mango", "berry",
    "storm", "cloud", "rain", "sun", "moon", "star", "sky", "ocean", "river",
    "fire", "stone", "tree", "flower", "grass", "hill", "mountain", "forest",
    "tiger", "lion", "bear", "wolf", "fox", "eagle", "hawk", "shark", "whale",
    "silver", "golden", "crystal", "thunder", "lightning", "shadow", "light",
    "snow", "frost", "flame", "ember", "breeze", "wind", "rainbow",

    # Космос и астрономия
    "galaxy", "nebula", "comet", "asteroid", "meteor", "planet", "orbit",
    "satellite", "eclipse", "aurora", "cosmos", "universe", "void", "zenith",
    "nadir", "equinox", "solstice", "zodiac", "horizon", "celestial", "lunar",
    "solar", "stellar", "galactic", "cosmic", "nebular",

    # География и природа
    "canyon", "delta", "fjord", "glacier", "gulf", "isthmus", "mesa", "oasis",
    "plateau", "prairie", "savanna", "tundra", "valley", "volcano", "waterfall",
    "wetland", "woodland", "grove", "thicket", "copse", "meadow", "pasture",
    "orchard", "vineyard", "garden", "hedge", "shrub", "fern", "moss", "lichen",
    "bloom", "blossom", "petal", "thorn", "vine", "root", "branch", "leaf",
    "trunk", "bark", "timber", "resin", "sap", "nectar", "pollen", "honey",
    "wax", "silk", "wool", "cotton", "linen", "hemp", "jute", "bamboo", "cane",
    "reed", "herb", "spice", "mint", "basil", "thyme", "rosemary", "sage",
    "oregano", "parsley", "dill", "fennel", "anise", "cumin", "turmeric",
    "cinnamon", "nutmeg", "clove", "cardamom", "vanilla", "cocoa", "coffee",
    "tea", "matcha",

    # Животные
    "panther", "leopard", "jaguar", "cheetah", "cougar", "lynx", "bobcat",
    "ocelot", "serval", "caracal", "civet", "genet", "mongoose", "meerkat",
    "hyena", "jackal", "coyote", "dingo", "panda", "koala", "kangaroo",
    "wallaby", "wombat", "platypus", "echidna", "hedgehog", "mole", "shrew",
    "bat", "raccoon", "skunk", "otter", "beaver", "muskrat", "porcupine",
    "armadillo", "sloth", "anteater", "tapir", "rhinoceros", "hippopotamus",
    "elephant", "mammoth", "mastodon", "giraffe", "zebra", "horse", "donkey",
    "mule", "camel", "llama", "alpaca", "vicuna", "guanaco", "goat", "sheep",
    "ram", "ewe", "lamb", "deer", "elk", "moose", "caribou", "reindeer",
    "antelope", "gazelle", "impala", "wildebeest", "buffalo", "bison", "yak",
    "ox", "cow", "bull", "calf", "pig", "hog", "boar", "warthog", "peccary",
    "rabbit", "hare", "pika", "squirrel", "chipmunk", "gopher", "prairie dog",
    "marmot", "groundhog", "mink", "weasel", "ferret", "marten", "sable",
    "ermine", "stoat", "badger", "wolverine", "rat", "mouse", "hamster",
    "gerbil", "vole", "lemming", "nutria", "coypu", "chinchilla", "degu",
    "falcon", "raven", "crow", "magpie", "jay", "finch", "sparrow", "robin",
    "bluebird", "cardinal", "oriole", "tanager", "warbler", "thrush",
    "blackbird", "starling", "myna", "parrot", "macaw", "cockatoo", "parakeet",
    "lovebird", "canary", "lark", "woodpecker", "toucan", "hornbill",
    "dolphin", "porpoise", "seal", "sea lion", "walrus", "manatee", "dugong",
    "ray", "manta", "stingray", "jellyfish", "octopus", "squid", "cuttlefish",
    "nautilus", "coral", "anemone", "starfish", "sea urchin",
    "butterfly", "dragonfly", "damselfly", "moth", "bee", "wasp", "hornet",
    "ant", "termite", "beetle", "ladybug", "firefly", "cricket", "grasshopper",
    "mantis",

    # Мифология и фэнтези
    "phoenix", "dragon", "griffin", "unicorn", "pegasus", "chimera", "sphinx",
    "centaur", "minotaur", "satyr", "nymph", "sprite", "fairy", "elf", "dwarf",
    "troll", "giant", "ogre", "goblin", "hobbit", "wizard", "witch", "sorcerer",
    "magician", "alchemist", "prophet", "oracle", "seer", "mystic", "shaman",
    "druid", "bard", "minstrel", "troubadour", "knight", "paladin", "ranger",
    "rogue", "assassin",

    # Абстрактные понятия
    "freedom", "justice", "peace", "glory", "honor", "valor", "courage",
    "strength", "power", "might", "force", "energy", "spirit", "soul", "heart",
    "mind", "will", "faith", "hope", "love", "joy", "bliss", "ecstasy",
    "rapture", "serenity", "tranquility", "harmony", "balance", "order",
    "chaos", "infinity", "eternity", "destiny", "fate", "karma", "dharma",
    "nirvana", "enlightenment", "wisdom", "knowledge", "truth", "beauty",
    "grace", "mercy", "compassion", "empathy", "sympathy", "kindness",
    "generosity", "charity", "humility", "patience", "diligence", "prudence",
    "temperance", "fortitude",

    # Цвета и оттенки
    "crimson", "scarlet", "ruby", "garnet", "mahogany", "chestnut", "auburn",
    "copper", "bronze", "platinum", "chrome", "steel", "iron", "pewter",
    "cobalt", "titanium", "mercury", "jade", "emerald", "malachite", "turquoise",
    "aqua", "cyan", "cerulean", "sapphire", "lapis", "azure", "indigo",
    "violet", "purple", "mauve", "lilac", "lavender", "plum", "orchid",
    "magenta", "fuchsia", "pink", "rose", "coral", "apricot", "tangerine",
    "amber", "butterscotch", "caramel", "chocolate", "mocha", "espresso",
    "cream", "ivory", "pearl", "alabaster", "snowy", "ash", "slate", "charcoal",
    "obsidian", "ebony", "jet",

    # Еда и напитки
    "cherry", "plum", "nectarine", "melon", "cantaloupe", "honeydew",
    "watermelon", "lime", "lemon", "grapefruit", "pomegranate", "persimmon",
    "fig", "date", "olive", "avocado", "coconut", "almond", "walnut", "pecan",
    "hazelnut", "pistachio", "cashew", "macadamia",

    # Технологии и наука
    "cyber", "digital", "virtual", "quantum", "photon", "electron", "neutron",
    "proton", "quark", "gluon", "boson", "laser", "radar", "sonar", "pixel",
    "vector", "matrix", "algorithm", "cipher", "code", "encrypt", "decrypt",
    "firewall", "gateway", "router", "server", "data", "info", "memory",
    "cache", "buffer", "stream", "pulse", "frequency", "amplitude",

    # Музыка и звук
    "melody", "harmony", "rhythm", "beat", "tempo", "pitch", "tone", "chord",
    "scale", "octave", "symphony", "concerto", "sonata", "ballad", "opera",
    "aria", "serenade", "nocturne", "rhapsody", "etude", "fugue", "canon",
    "round", "blues", "jazz", "rock", "pop", "folk", "country", "soul",
    "funk", "reggae", "ska", "punk", "metal", "indie", "alternative",

    # Эмоции и чувства
    "happiness", "sadness", "anger", "fear", "surprise", "disgust", "anticipation",
    "trust", "desire", "passion", "zeal", "zest", "gusto", "fervor", "ardor",
    "enthusiasm", "excitement", "thrill", "adventure", "mystery", "wonder",
    "awe", "reverence", "devotion", "loyalty", "fidelity", "honesty",
    "sincerity", "integrity", "dignity", "nobility",

    # Действия и явления
    "blaze", "flare", "flash", "spark", "glow", "gleam", "shimmer", "glisten",
    "sparkle", "twinkle", "glimmer", "glitter", "shine", "radiate", "illuminate",
    "beam", "ray", "burst", "surge", "rush", "flow", "cascade", "torrent",
    "flood", "tide", "ripple", "splash", "spray", "mist", "vapor", "smoke",
    "fume", "earthquake", "tremor", "eruption", "avalanche", "landslide",
    "mudslide", "rockfall", "sinkhole", "geyser", "hot spring"
]