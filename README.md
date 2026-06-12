# AI_Learning
For Learning
Month	Week	Focus Area	Core Concepts	Math/Theory Assignment	Coding / LeetCode Challenge	Tech Stack
Month 1	Week 1	Linear Algebra Core	Vectors, Matrices, Dot Products, Matrix Multiplication, Broadcasting.	By hand: Multiply two 3x3 matrices. Calculate the dot product of two vectors. Prove matrix multiplication is not commutative.	"LC 73: Set Matrix Zeroes.
LC 867: Transpose Matrix.
C++: Write a generic Matrix class with overloaded operators."	C++, Python (NumPy)
Month 1	Week 2	Advanced Linear Algebra	Eigenvalues, Eigenvectors, Determinants, Intro to SVD and PCA.	Find the eigenvalues and eigenvectors of a 2x2 matrix by hand. Geometrically interpret what an eigenvector represents.	"LC 54: Spiral Matrix.
Python: Implement PCA from scratch using NumPy and reduce a 2D dataset to 1D."	Python (NumPy, Matplotlib)
Month 1	Week 3	Calculus for Machine Learning	Derivatives, Partial Derivatives, The Chain Rule, Gradients.	By hand: Calculate the partial derivatives for f(x,y) = x^2 * y + y^3. Apply the Chain Rule to a nested function.	"LC 69: Sqrt(x) (Implement using Newton's Method - purely calculus based optimization).
Python: Implement a basic Gradient Descent algorithm to find the minimum of y = (x-3)^2."	Python
Month 1	Week 4	Probability & Statistics	Probability Distributions (Normal, Binomial), Variance, Bayes' Theorem.	Calculate the expected value and variance of a given dataset. Solve a conditional probability problem using Bayes' Theorem.	"LC 122: Best Time to Buy and Sell Stock II (Greedy optimization).
Java: Build a Naive Bayes text classifier from scratch for spam detection."	Java, Python (SciPy)
Month 2	Week 5	Linear & Logistic Regression	Ordinary Least Squares, Sigmoid Function, Maximum Likelihood Estimation.	Derive the gradient update rule for Logistic Regression using Binary Cross Entropy loss.	"LC 149: Max Points on a Line (Geometry/Slopes).
Python: Train a Linear Regression model using Scikit-Learn."	Python (Scikit-Learn)
Month 2	Week 6	SVMs & Tree Ensembles	Hyperplanes, Kernel Trick, Gini Impurity, Entropy, Random Forests.	Calculate the Gini Impurity for a small dataset split to understand how a Decision Tree selects nodes.	"LC 108: Convert Sorted Array to Binary Search Tree.
Python: Implement a simple Decision Tree split algorithm."	Python
Month 2	Week 7	Unsupervised Learning	K-Means Clustering, K-Nearest Neighbors, Silhouette Score.	Trace the K-Means algorithm by hand for 4 data points and K=2 over two iterations.	"LC 973: K Closest Points to Origin (Priority Queue / Distances).
Python: Implement K-Means from scratch without using Scikit-Learn."	Python, Java
Month 2	Week 8	Classical ML Project	Model serialization, REST APIs, Feature Engineering.	Analyze the ROC-AUC curve of your trained model. What does a false positive cost in your specific domain?	Project: Train a predictive model (e.g., fraud detection), export to ONNX/PMML, and serve via Java Spring Boot API.	Python, Java Spring Boot
Month 3	Week 9	Neural Network Fundamentals	Perceptrons, MLPs, Activation Functions (ReLU, Softmax), Forward Pass.	Manually calculate the forward pass of a 2-2-1 neural network given specific weights and inputs.	C++: Implement a multi-dimensional array or basic Tensor class to hold network weights.	C++
Month 3	Week 10	Backpropagation & PyTorch	Computational Graphs, Backpropagation, Loss Functions, Optimizers (Adam).	Derive the backpropagation equations for a 2-layer network. (This is the most critical math week).	"LC 133: Clone Graph (Understanding computational graph traversal).
Python: Build your first MLP using PyTorch."	Python (PyTorch)
Month 3	Week 11	Computer Vision & CNNs	Convolutions, Filters, Pooling, Stride, Padding.	Calculate the output dimensions of an image passing through a specific Conv2D layer.	"LC 200: Number of Islands (Grid traversal).
Python: Train a CNN on MNIST or CIFAR-10 using PyTorch."	Python (PyTorch)
Month 3	Week 12	Autograd Challenge Project	Low-level memory management, exact math implementations of AI.	Verify your C++ gradient calculations against PyTorch's autograd outputs.	Project: Build a 2-layer neural network completely from scratch in C++. Implement both forward and backward passes.	C++
Month 4	Week 13	Sequence Models & Embeddings	RNNs, Word2Vec, Embeddings, Tokenization.	Understand cosine similarity mathematically as it applies to word vectors.	LC 208: Implement Trie (Prefix Tree) - useful for vocabulary/tokenization concepts.	Python
Month 4	Week 14	The Attention Mechanism	Self-Attention, Query/Key/Value matrices, Scaled Dot-Product Attention.	Calculate the attention scores for a 3-word sentence given predefined Q, K, and V matrices.	"LC 43: Multiply Strings.
Python: Implement the Scaled Dot-Product Attention function from scratch using PyTorch tensors."	Python (PyTorch)
Month 4	Week 15	Transformer Architectures	Encoder/Decoder stacks, Positional Encoding, Multi-Head Attention.	Map out the exact tensor shape transformations occurring through one entire Transformer block.	Python: Build a basic Transformer Encoder block in PyTorch following the 'Attention is All You Need' paper.	Python (PyTorch)
Month 4	Week 16	Fine-Tuning & LLMs	Transfer Learning, Hugging Face Hub, LoRA (Low-Rank Adaptation).	Read and summarize the LoRA paper. Why does low-rank matrix decomposition save memory?	Project: Fine-tune a BERT model on a custom dataset using Hugging Face Transformers and PyTorch.	Python (Hugging Face)
Month 5	Week 17	Retrieval-Augmented Generation (RAG)	Vector Databases, Semantic Search, Document Chunking strategies.	Compare the mathematical differences and use cases of L2 distance, Cosine Similarity, and Inner Product.	Java: Set up a local Vector DB (e.g., Milvus or FAISS via wrapper) and ingest chunked text documents.	Java, Vector DB
Month 5	Week 18	Prompt Engineering & Orchestration	Chain of Thought, Few-Shot, LangChain, LlamaIndex.	Analyze the token cost equations for various API calls. Design an optimization strategy.	"LC 380: Insert Delete GetRandom O(1).
Python: Build a multi-step LangChain pipeline that queries a database and summarizes the result."	Python (LangChain)
Month 5	Week 19	Agentic AI & Tool Use	Function calling, ReAct architecture, autonomous routing.	Design a finite state machine (FSM) that dictates an AI agent's decision loop.	Python/Java: Build an agent that can decide whether to query a calculator function or a search function based on user input.	Python or Java
Month 5	Week 20	Blueprint Agent Project	System design, robust JSON parsing, rule engines.	Design the system architecture for a highly concurrent multi-agent system.	Project: Build an AI pipeline that extracts unstructured text, applies natural language rules, and outputs standardized JSON.	Java or Python
Month 6	Week 21	Model Optimization & Quantization	FP32 to FP16/INT8 conversion, Model Pruning, ONNX.	Calculate the memory footprint difference of a 1 Billion parameter model in FP32 vs INT8.	"LC 191: Number of 1 Bits (Bit manipulation).
Python: Convert your fine-tuned Transformer model from Week 16 into ONNX format."	Python, ONNX
Month 6	Week 22	Hardware Accelerators & APIs	CUDA basics, TensorRT, vLLM, memory bandwidth bottlenecks.	Understand the difference between compute-bound and memory-bound operations in AI.	C++: Write a basic CUDA kernel to add two large arrays to understand GPU parallelization.	C++, CUDA
Month 6	Week 23	High-Performance Edge Inference	ONNX Runtime C++ API, memory pooling, multi-threading.	Analyze the latency vs throughput tradeoff curves for different batch sizes.	Project: Write a C++ wrapper using ONNX Runtime to load and execute inference on your model. Benchmark it against Python.	C++
Month 6	Week 24	Final Capstone Integration	Microservices, gRPC, Docker.	Final review of the mathematics: Write a one-page summary of how an input token becomes an output token in a Transformer.	Wrap your C++ inference engine in a Docker container and expose it via a Java Spring Boot / gRPC frontend.	Java, C++, Docker
