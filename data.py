# data.py — All hardcoded curriculum content for Amrita CSE Navigator

# ─── Semester-wise curriculum ───────────────────────────────────────────────
CURRICULUM = {
    1: [
        {"name": "Technical Communication", "career": "All roles – communication is key"},
        {"name": "Calculus", "career": "Foundation for ML, AI, and Engineering"},
        {"name": "Computational Problem Solving", "career": "Core programming – Product companies"},
        {"name": "Electrical and Electronics Engineering", "career": "Embedded Systems, IoT"},
        {"name": "Computer Hardware Essentials", "career": "Systems, Hardware Roles"},
    ],
    2: [
        {"name": "Discrete Mathematics", "career": "Algorithms, Cryptography, Theory of Computation"},
        {"name": "Linear Algebra", "career": "Machine Learning, Data Science, Graphics"},
        {"name": "Object Oriented Programming", "career": "Software Development – All roles"},
        {"name": "User Interface Design", "career": "Frontend, Product Design, UX Roles"},
    ],
    3: [
        {"name": "Data Structures and Algorithms", "career": "Critical for Product-Based Companies"},
        {"name": "Database Management Systems", "career": "Backend, Data Engineering, Analytics"},
        {"name": "Procedural Programming using C", "career": "Systems Programming, Embedded"},
        {"name": "Digital Electronics", "career": "VLSI, Embedded Systems, Hardware"},
        {"name": "Optimization Techniques", "career": "Operations Research, ML, Finance"},
    ],
    4: [
        {"name": "Design and Analysis of Algorithms", "career": "FAANG Interviews, Competitive Programming"},
        {"name": "Operating Systems", "career": "Core Systems, Infra, Cloud, Interviews"},
        {"name": "Computer Organization and Architecture", "career": "Systems Design, VLSI"},
        {"name": "Probability and Random Processes", "career": "AI, ML, Data Science, Quant"},
        {"name": "Functional Languages", "career": "Functional Programming, Research, Finance"},
    ],
    5: [
        {"name": "Machine Learning", "career": "AI/ML Engineer, Data Scientist"},
        {"name": "Computer Networks", "career": "Network Engineering, Cloud, Security"},
        {"name": "Theory of Computation", "career": "Compiler Design, Research, Formal Methods"},
        {"name": "Embedded Systems", "career": "IoT, Robotics, Autonomous Systems"},
    ],
    6: [
        {"name": "Software Engineering", "career": "Product Management, Dev Leads, Full Stack"},
        {"name": "Distributed Systems", "career": "Cloud, Backend, SRE, System Design"},
        {"name": "Foundations of Cyber Security", "career": "Security Analyst, Ethical Hacker"},
        {"name": "Compiler Design", "career": "Programming Language Design, Research"},
        {"name": "Project Phase I", "career": "Research, Startup, Industry Project Experience"},
    ],
    7: [
        {"name": "AI Fundamentals", "career": "AI Engineer, Research, Automation"},
        {"name": "Professional Electives", "career": "Based on specialization chosen"},
        {"name": "Project Phase II", "career": "Deep domain expertise, Publications"},
    ],
    8: [
        {"name": "Final Year Project Phase III", "career": "Portfolio, Industry Ready, Research Publications"},
    ],
}

# ─── Subject → Career Reason mapping ────────────────────────────────────────
CAREER_MAP = {
    "Data Structures and Algorithms": "The #1 skill tested in product-based company interviews (Google, Amazon, Microsoft). Mastering DSA is non-negotiable for placements.",
    "Database Management Systems": "Every backend system uses databases. Essential for Data Engineering, Backend Development, and Analytics roles.",
    "Operating Systems": "Core OS concepts (processes, threads, memory, scheduling) are heavily tested in systems interviews and essential for Cloud/Infra roles.",
    "Machine Learning": "The backbone of AI products. Required for AI/ML Engineer, Data Scientist, and Research roles.",
    "Computer Networks": "Essential for Cloud Computing, Cyber Security, Network Engineering, and understanding of distributed systems.",
    "Foundations of Cyber Security": "Entry point to Security Analyst, Penetration Tester, and Ethical Hacker roles.",
    "Design and Analysis of Algorithms": "Advanced problem solving for FAANG-level interviews and algorithm research.",
    "Distributed Systems": "Critical for backend system design interviews and building scalable cloud applications.",
    "Software Engineering": "Covers SDLC, Agile, Design Patterns – core for any software development or product role.",
    "AI Fundamentals": "Provides conceptual grounding for AI Engineering, Automation, and Research careers.",
    "Linear Algebra": "Foundation mathematics used in ML models, computer graphics, and signal processing.",
    "Probability and Random Processes": "Mathematical foundation for Statistics, ML/AI, Data Science, and Quantitative Finance.",
    "Object Oriented Programming": "Foundation of modern software development across all languages and domains.",
    "Compiler Design": "Deep technical knowledge valued in systems programming, language design, and research.",
    "Embedded Systems": "Core for IoT, Robotics, Autonomous Vehicles, and Hardware-Software integration.",
    "Calculus": "Used in optimization (gradient descent), physics simulations, and ML training algorithms.",
    "Discrete Mathematics": "Underpins algorithms, cryptography, logic, and theoretical computer science.",
    "Theory of Computation": "Foundation for understanding limits of computation, formal verification, and compiler theory.",
    "Computer Organization and Architecture": "Crucial for understanding CPU design, VLSI, performance optimization.",
    "Technical Communication": "Essential for interviews, technical writing, team collaboration, and leadership.",
    "User Interface Design": "Core for Frontend Engineering, UX/Product Design, and startup founders.",
    "Functional Languages": "Valued in functional programming paradigms used in finance, research, and modern languages.",
    "Digital Electronics": "Foundation for VLSI, FPGA, Embedded design, and hardware engineering.",
    "Optimization Techniques": "Applied in operations research, scheduling, ML hyperparameter tuning.",
    "Computational Problem Solving": "Builds logical thinking and programming foundations for all CS careers.",
    "Electrical and Electronics Engineering": "Essential for Embedded Systems, IoT, and Hardware-Software co-design.",
    "Computer Hardware Essentials": "Fundamental knowledge for systems programming and hardware roles.",
    "Project Phase I": "First hands-on industry/research project – builds portfolio and practical skills.",
    "Project Phase II": "Advanced project work leading to publications or startup prototype.",
    "Final Year Project Phase III": "Capstone project – primary asset for placements and higher studies.",
    "Professional Electives": "Specialization courses tailored to your chosen career path.",
}

# ─── Specialization → Elective mapping ──────────────────────────────────────
ELECTIVE_MAP = {
    "Artificial Intelligence": [
        {"name": "Neural Networks and Deep Learning", "desc": "Covers CNNs, RNNs, Transformers and modern architectures"},
        {"name": "Natural Language Processing", "desc": "Text processing, BERT, GPT, sentiment analysis, chatbots"},
        {"name": "Generative AI", "desc": "GANs, VAEs, Diffusion models, large language models"},
        {"name": "Reinforcement Learning", "desc": "Q-Learning, policy gradients, multi-agent systems"},
        {"name": "Machine Learning with Graphs", "desc": "Graph Neural Networks, knowledge graphs, recommendation systems"},
    ],
    "Cyber Security": [
        {"name": "Cryptography and Network Security", "desc": "Encryption algorithms, PKI, TLS, digital signatures"},
        {"name": "Information Security Management", "desc": "ISO 27001, risk assessment, security policies"},
        {"name": "Secure Coding Practices", "desc": "OWASP Top 10, code auditing, secure SDLC"},
        {"name": "Cyber Forensics", "desc": "Digital evidence collection, malware analysis, incident response"},
        {"name": "Secure Networks and Protocols", "desc": "Firewalls, VPNs, IDS/IPS, zero trust architecture"},
    ],
    "Data Science": [
        {"name": "Big Data Analytics", "desc": "Hadoop, Spark, MapReduce, distributed data processing"},
        {"name": "Data Visualization and Storytelling", "desc": "Matplotlib, Seaborn, Tableau, D3.js, dashboard design"},
        {"name": "Mining Massive Datasets", "desc": "Clustering, frequent patterns, PageRank, recommendation engines"},
        {"name": "Time Series Forecasting", "desc": "ARIMA, Prophet, LSTM for temporal data analysis"},
        {"name": "Statistical Learning Theory", "desc": "Bayesian methods, hypothesis testing, probabilistic models"},
    ],
    "Product-Based Companies": [
        {"name": "Advanced Data Structures", "desc": "Segment trees, Fenwick trees, advanced graph algorithms"},
        {"name": "System Design", "desc": "Scalable systems, microservices, databases at scale"},
        {"name": "Competitive Programming", "desc": "Algorithmic problem solving for coding competitions"},
        {"name": "Cloud Computing", "desc": "AWS/GCP/Azure services, serverless, containers"},
        {"name": "DevOps and CI/CD", "desc": "Docker, Kubernetes, Jenkins, GitHub Actions"},
    ],
    "Research": [
        {"name": "Advanced Algorithms", "desc": "Approximation algorithms, randomized algorithms, complexity theory"},
        {"name": "Formal Methods", "desc": "Model checking, theorem proving, formal verification"},
        {"name": "Quantum Computing", "desc": "Qubits, quantum gates, Shor's algorithm, NISQ devices"},
        {"name": "High Performance Computing", "desc": "Parallel programming, CUDA, MPI, GPU acceleration"},
        {"name": "Bio-Inspired Computing", "desc": "Evolutionary algorithms, swarm intelligence, neural computation"},
    ],
    "Startup": [
        {"name": "Full Stack Web Development", "desc": "React, Node.js, REST APIs, deployment, scalability"},
        {"name": "Mobile App Development", "desc": "React Native, Flutter, iOS/Android development"},
        {"name": "Product Management", "desc": "Roadmapping, user research, agile sprints, metrics"},
        {"name": "Business Analytics", "desc": "KPIs, cohort analysis, A/B testing, decision making"},
        {"name": "Cloud and Infrastructure", "desc": "Scalable deployments, cost optimization, serverless"},
    ],
}

# ─── Elective roadmap (semester-wise recommendation) ───────────────────────
ELECTIVE_ROADMAP = {
    "Artificial Intelligence": {
        5: ["Machine Learning (Core)", "Neural Networks and Deep Learning"],
        6: ["Natural Language Processing", "Reinforcement Learning"],
        7: ["Generative AI", "Machine Learning with Graphs"],
        8: ["Final Project: AI Application"],
    },
    "Cyber Security": {
        5: ["Computer Networks (Core)", "Cryptography and Network Security"],
        6: ["Foundations of Cyber Security (Core)", "Information Security Management"],
        7: ["Cyber Forensics", "Secure Networks and Protocols"],
        8: ["Final Project: Security Audit / CTF"],
    },
    "Data Science": {
        5: ["Machine Learning (Core)", "Statistical Learning Theory"],
        6: ["Big Data Analytics", "Data Visualization and Storytelling"],
        7: ["Mining Massive Datasets", "Time Series Forecasting"],
        8: ["Final Project: End-to-End Data Pipeline"],
    },
    "Product-Based Companies": {
        3: ["Data Structures and Algorithms (Core)"],
        4: ["Design and Analysis of Algorithms (Core)", "Advanced Data Structures"],
        5: ["System Design", "Competitive Programming"],
        6: ["Cloud Computing", "DevOps and CI/CD"],
        7: ["Mock Interviews", "Open Source Contributions"],
        8: ["Final Project: Scalable System"],
    },
    "Research": {
        4: ["Theory of Computation (Core)", "Formal Methods"],
        5: ["Advanced Algorithms", "Quantum Computing"],
        6: ["High Performance Computing"],
        7: ["Bio-Inspired Computing", "Research Paper"],
        8: ["Final Project: Conference Publication"],
    },
    "Startup": {
        3: ["Full Stack Web Development"],
        4: ["Mobile App Development", "Product Management"],
        5: ["Cloud and Infrastructure", "Business Analytics"],
        6: ["Building MVP + Launch"],
        7: ["Scaling Product + Fundraising basics"],
        8: ["Final Project: Live Product"],
    },
}

# ─── Subject details: topics + YouTube video links ──────────────────────────
SUBJECT_DETAILS = {
    "Data Structures and Algorithms": {
        "topics": [
            {
                "name": "Arrays and Strings",
                "subtopics": ["Array traversal", "Sliding window", "Two pointers", "String manipulation"],
            },
            {
                "name": "Linked Lists",
                "subtopics": ["Singly linked list", "Doubly linked list", "Circular linked list", "Fast/slow pointers"],
            },
            {
                "name": "Stacks and Queues",
                "subtopics": ["Stack operations", "Queue using arrays", "Monotonic stack", "Circular queue"],
            },
            {
                "name": "Trees",
                "subtopics": ["Binary trees", "BST", "AVL trees", "Tree traversals", "Segment trees"],
            },
            {
                "name": "Graphs",
                "subtopics": ["BFS", "DFS", "Dijkstra", "Floyd-Warshall", "Topological sort", "Union-Find"],
            },
            {
                "name": "Dynamic Programming",
                "subtopics": ["Memoization", "Tabulation", "0/1 Knapsack", "LCS", "LIS", "DP on trees"],
            },
            {
                "name": "Sorting and Searching",
                "subtopics": ["Merge sort", "Quick sort", "Heap sort", "Binary search variants"],
            },
        ],
        "video_url": "https://www.youtube.com/embed/pkYVOmU3MgA",
    },
    "Database Management Systems": {
        "topics": [
            {"name": "ER Model", "subtopics": ["Entities and Attributes", "Relationships", "ER to Relational mapping"]},
            {"name": "Relational Model", "subtopics": ["Keys", "Relational algebra", "Relational calculus"]},
            {"name": "SQL", "subtopics": ["DDL", "DML", "Joins", "Subqueries", "Aggregation", "Views"]},
            {"name": "Normalization", "subtopics": ["1NF, 2NF, 3NF", "BCNF", "Decomposition"]},
            {"name": "Transactions", "subtopics": ["ACID properties", "Concurrency control", "Deadlock", "Isolation levels"]},
            {"name": "Indexing and Storage", "subtopics": ["B+ Trees", "Hash indexing", "Query optimization"]},
            {"name": "NoSQL Databases", "subtopics": ["MongoDB basics", "CAP theorem", "Key-Value stores"]},
        ],
        "video_url": "https://www.youtube.com/embed/HXV3zeQKqGY",
    },
    "Operating Systems": {
        "topics": [
            {"name": "Process Management", "subtopics": ["Process vs Thread", "PCB", "Context switching", "Process states"]},
            {"name": "CPU Scheduling", "subtopics": ["FCFS", "SJF", "Round Robin", "Priority scheduling", "Multilevel queues"]},
            {"name": "Memory Management", "subtopics": ["Paging", "Segmentation", "Virtual memory", "Page replacement algorithms"]},
            {"name": "Synchronization", "subtopics": ["Race conditions", "Mutex", "Semaphores", "Deadlock avoidance"]},
            {"name": "File Systems", "subtopics": ["File allocation", "Directory structure", "Inodes", "FAT/NTFS/ext4"]},
            {"name": "I/O Management", "subtopics": ["Device drivers", "DMA", "I/O scheduling", "RAID"]},
        ],
        "video_url": "https://www.youtube.com/embed/vBURTt97EkA",
    },
    "Machine Learning": {
        "topics": [
            {"name": "Linear Regression", "subtopics": ["Simple linear regression", "Multiple regression", "Gradient descent", "Regularization"]},
            {"name": "Classification", "subtopics": ["Logistic Regression", "Decision Trees", "Random Forests", "SVM", "KNN"]},
            {"name": "Clustering", "subtopics": ["K-Means", "Hierarchical clustering", "DBSCAN", "Gaussian Mixture Models"]},
            {"name": "Dimensionality Reduction", "subtopics": ["PCA", "LDA", "t-SNE", "Autoencoders"]},
            {"name": "Neural Networks", "subtopics": ["Perceptron", "Backpropagation", "Activation functions", "Optimizers"]},
            {"name": "Model Evaluation", "subtopics": ["Train/test split", "Cross-validation", "Confusion matrix", "ROC/AUC"]},
        ],
        "video_url": "https://www.youtube.com/embed/GwIo3gDZCVQ",
    },
    "Computer Networks": {
        "topics": [
            {"name": "OSI Model", "subtopics": ["7 layers overview", "Data encapsulation", "Protocol stack"]},
            {"name": "TCP/IP", "subtopics": ["TCP handshake", "UDP vs TCP", "IP addressing", "Subnetting", "NAT"]},
            {"name": "Application Layer", "subtopics": ["HTTP/HTTPS", "DNS", "SMTP", "FTP", "WebSockets"]},
            {"name": "Network Security", "subtopics": ["SSL/TLS", "Firewalls", "VPN", "IDS/IPS"]},
            {"name": "Routing and Switching", "subtopics": ["OSPF", "BGP", "VLANs", "Spanning Tree Protocol"]},
            {"name": "Wireless Networks", "subtopics": ["WiFi standards", "Cellular networks", "Bluetooth", "IoT protocols"]},
        ],
        "video_url": "https://www.youtube.com/embed/qiQR5rTSshw",
    },
    "Object Oriented Programming": {
        "topics": [
            {"name": "OOP Concepts", "subtopics": ["Classes and Objects", "Encapsulation", "Abstraction", "Inheritance", "Polymorphism"]},
            {"name": "Design Patterns", "subtopics": ["Singleton", "Factory", "Observer", "Strategy", "Decorator"]},
            {"name": "Exception Handling", "subtopics": ["Try/Catch", "Custom exceptions", "Finally block"]},
            {"name": "Collections", "subtopics": ["Lists", "Maps", "Sets", "Streams (Java)"]},
            {"name": "File I/O", "subtopics": ["Reading/writing files", "Serialization", "Streams"]},
        ],
        "video_url": "https://www.youtube.com/embed/Ej_02ICOIgs",
    },
    "Design and Analysis of Algorithms": {
        "topics": [
            {"name": "Complexity Analysis", "subtopics": ["Big-O, Omega, Theta", "Recurrence relations", "Master theorem"]},
            {"name": "Divide and Conquer", "subtopics": ["Merge sort", "Quick sort", "Binary search", "Strassen's matrix multiplication"]},
            {"name": "Greedy Algorithms", "subtopics": ["Activity selection", "Huffman coding", "Kruskal's/Prim's MST"]},
            {"name": "Dynamic Programming", "subtopics": ["Matrix chain multiplication", "Longest common subsequence", "Bellman-Ford"]},
            {"name": "Graph Algorithms", "subtopics": ["Shortest paths", "Network flow", "Bipartite matching"]},
            {"name": "NP Completeness", "subtopics": ["P vs NP", "Reductions", "Approximation algorithms"]},
        ],
        "video_url": "https://www.youtube.com/embed/0IAPZzGSbME",
    },
    "Foundations of Cyber Security": {
        "topics": [
            {"name": "Security Fundamentals", "subtopics": ["CIA Triad", "Threat modeling", "Attack surfaces", "Security policies"]},
            {"name": "Cryptography Basics", "subtopics": ["Symmetric encryption", "Asymmetric encryption", "Hash functions", "Digital signatures"]},
            {"name": "Network Security", "subtopics": ["Firewalls", "VPNs", "Intrusion detection", "Packet analysis"]},
            {"name": "Web Security", "subtopics": ["OWASP Top 10", "SQL Injection", "XSS", "CSRF", "Authentication flaws"]},
            {"name": "Ethical Hacking", "subtopics": ["Penetration testing", "Kali Linux tools", "Vulnerability assessment"]},
        ],
        "video_url": "https://www.youtube.com/embed/3Kq1MIfTWCE",
    },
    "Software Engineering": {
        "topics": [
            {"name": "SDLC Models", "subtopics": ["Waterfall", "Agile", "Scrum", "Kanban", "Spiral model"]},
            {"name": "Requirements Engineering", "subtopics": ["Use cases", "User stories", "Requirements specification"]},
            {"name": "Design Principles", "subtopics": ["SOLID principles", "DRY", "KISS", "UML diagrams"]},
            {"name": "Testing", "subtopics": ["Unit testing", "Integration testing", "TDD", "BDD", "Selenium"]},
            {"name": "DevOps", "subtopics": ["CI/CD pipelines", "Docker", "Git workflows", "Release management"]},
        ],
        "video_url": "https://www.youtube.com/embed/l1ze4JuBYsQ",
    },
    "AI Fundamentals": {
        "topics": [
            {"name": "Search Algorithms", "subtopics": ["BFS/DFS in AI", "A* search", "Heuristics", "Minimax"]},
            {"name": "Knowledge Representation", "subtopics": ["Propositional logic", "First-order logic", "Ontologies"]},
            {"name": "Planning", "subtopics": ["STRIPS", "State-space search", "Goal-based agents"]},
            {"name": "Machine Learning Overview", "subtopics": ["Supervised/Unsupervised", "Reinforcement learning intro"]},
            {"name": "Deep Learning", "subtopics": ["CNNs", "RNNs", "Transformers", "Transfer learning"]},
            {"name": "AI Ethics", "subtopics": ["Bias in AI", "Explainability", "AI governance", "Responsible AI"]},
        ],
        "video_url": "https://www.youtube.com/embed/JMUxmLyrhSk",
    },
    "Discrete Mathematics": {
        "topics": [
            {"name": "Set Theory", "subtopics": ["Sets, subsets, power sets", "Set operations", "Venn diagrams"]},
            {"name": "Logic", "subtopics": ["Propositional logic", "Predicates", "Quantifiers", "Proof techniques"]},
            {"name": "Graph Theory", "subtopics": ["Graphs, trees, paths", "Euler/Hamiltonian paths", "Planar graphs"]},
            {"name": "Combinatorics", "subtopics": ["Permutations", "Combinations", "Pigeonhole principle", "Inclusion-exclusion"]},
            {"name": "Algebraic Structures", "subtopics": ["Groups", "Rings", "Fields", "Lattices"]},
        ],
        "video_url": "https://www.youtube.com/embed/rdXw7Ps9vxc",
    },
    "Distributed Systems": {
        "topics": [
            {"name": "Fundamentals", "subtopics": ["CAP theorem", "Consistency models", "Distributed clocks"]},
            {"name": "Consensus Algorithms", "subtopics": ["Paxos", "Raft", "Byzantine fault tolerance"]},
            {"name": "Replication", "subtopics": ["Leader-follower", "Quorum", "Conflict resolution"]},
            {"name": "Microservices", "subtopics": ["Service discovery", "API gateway", "Circuit breaker", "gRPC"]},
            {"name": "Message Queues", "subtopics": ["Kafka", "RabbitMQ", "Event-driven architecture"]},
        ],
        "video_url": "https://www.youtube.com/embed/UEAMfLPZZhE",
    },
}

# Default video for subjects without specific entries
DEFAULT_VIDEO_URL = "https://www.youtube.com/embed/rfscVS0vtbw"

DEFAULT_TOPICS = [
    {"name": "Introduction", "subtopics": ["Overview", "History", "Applications", "Real-world use cases"]},
    {"name": "Core Concepts", "subtopics": ["Fundamentals", "Key algorithms", "Theoretical background"]},
    {"name": "Practical Implementation", "subtopics": ["Coding examples", "Lab exercises", "Mini projects"]},
    {"name": "Advanced Topics", "subtopics": ["Research directions", "Industry applications", "Interview questions"]},
]

def get_subject_details(subject_name):
    """Return subject details, falling back to defaults if not found."""
    if subject_name in SUBJECT_DETAILS:
        return SUBJECT_DETAILS[subject_name]
    # Build default entry
    lang_pref = "Python"
    return {
        "topics": DEFAULT_TOPICS,
        "video_url": DEFAULT_VIDEO_URL,
    }

def get_all_subjects_flat():
    """Return a flat list of all subjects across all semesters."""
    subjects = []
    for sem, subs in CURRICULUM.items():
        for s in subs:
            subjects.append({"semester": sem, "name": s["name"], "career": s["career"]})
    return subjects
