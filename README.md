# E-commerce Data Engineering Pipeline - Hands-On Course

Welcome to the comprehensive data engineering course! This project will take you through building a complete, production-ready data pipeline from scratch using modern tools and cloud services.

## Course Overview

This hands-on course teaches you to build an end-to-end data engineering pipeline that processes e-commerce data using industry-standard tools. You'll go from raw data to actionable insights while learning best practices used by data engineering teams worldwide.

### What You'll Build:
1. **Data Pipeline**: Complete ETL process with synthetic e-commerce data
2. **Cloud Integration**: AWS S3 data lake for scalable storage
3. **Workflow Orchestration**: Professional orchestration with Prefect
4. **Containerization**: Production-ready Docker deployment
5. **Data Processing**: Advanced transformations and business metrics

## Architecture Diagram

```
📊 Sample Data    →    📤 S3 Upload    →    🧹 Processing    →    📈 Metrics    →    ☁️ S3 Storage
    (CSV Files)         (Raw Data)         (Transform)        (Analytics)       (Processed)
        ↓                    ↓                  ↓                  ↓                ↓
   Python Scripts    →   boto3/S3 API    →   Pandas/ETL     →   Aggregations  →  Data Lake
                                              ↓
                                         🔄 Prefect Flows (Orchestration)
                                              ↓
                                         🐳 Docker Containers (Production)
```

## 🛠️ Technology Stack

| Category | Technology | Purpose |
|----------|------------|---------|
| **Language** | Python 3.12 | Core development language |
| **Cloud Platform** | AWS S3 | Scalable data lake storage |
| **Orchestration** | Prefect 3.x | Workflow management & monitoring |
| **Data Processing** | Pandas, Polars | Data transformation & analysis |
| **Containerization** | Docker + Docker Compose | Production deployment |
| **Data Validation** | Great Expectations | Data quality assurance |
| **Package Management** | pip, requirements.txt | Dependency management |

## Project Structure

```
Hands-On-Project/
├── 📄 .env                              # AWS credentials (create this!)
├── 📊 data/                             # Sample datasets
│   ├── raw/                             # Raw CSV files
│   ├── customers.csv                    # Customer data
│   ├── products.csv                     # Product catalog
│   ├── orders.csv                       # Order transactions
│   ├── order_items.csv                  # Order line items
│   └── reviews.csv                      # Customer reviews
├── 🔧 data-pipeline/                    # Main pipeline code
│   ├── 📄 requirements.txt              # Python dependencies
│   ├── 🐳 docker-compose.yml            # Container orchestration
│   ├── 📂 src/                          # Source code
│   │   ├── data_ingestion/              # S3 upload scripts
│   │   │   └── s3_uploader.py           # Upload data to AWS S3
│   │   ├── data_processing/             # ETL transformations
│   │   │   └── etl_processor.py         # Clean & transform data
│   │   └── orchestration/               # Workflow management
│   │       └── prefect_flows.py         # Prefect orchestration
│   ├── 📂 config/                       # Configuration files
│   │   ├── aws_config.yaml              # AWS settings
│   │   ├── prefect_config.yaml          # Prefect configuration
│   │   └── data_schemas.yaml            # Data validation rules
│   ├── 📂 infrastructure/               # Container infrastructure
│   │   └── docker/
│   │       └── Dockerfile               # Container build instructions
│   └── 📂 tests/                        # Test files
│       └── test_aws_connection.py       # AWS connectivity tests
└── 📚 CONTAINERIZATION_GUIDE.md         # Complete Docker guide
```

## Quick Start Guide

### Prerequisites Checklist
- [ ] **Python 3.10+** installed (recommended: 3.12)
- [ ] **AWS Account** with S3 access
- [ ] **Docker Desktop** installed and running
- [ ] **Git** for version control
- [ ] **Text Editor** (VS Code recommended)

### Step 1: Environment Setup

1. **Clone/Download the project**
   ```bash
   cd "D:\Hands-On-Project"
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```

3. **Install dependencies**
   ```bash
   cd data-pipeline
   pip install -r requirements.txt
   ```

4. **Configure AWS credentials**
   Create `.env` file in project root:
   ```env
   AWS_ACCESS_KEY_ID=your_access_key_here
   AWS_SECRET_ACCESS_KEY=your_secret_key_here
   AWS_DEFAULT_REGION=us-east-1
   AWS_S3_BUCKET_NAME=your-unique-bucket-name
   ```

### 🔧 Step 2: Test Your Setup

1. **Test AWS connection**
   ```bash
   python tests/test_aws_connection.py
   ```
   ✅ Should show: "Connection successful!"

2. **Extract sample data**
   ```bash
   # Data should already be extracted in data/raw/ folder
   ls ../data/raw/  # Should show 5 CSV files
   ```

### 📤 Step 3: Run Data Pipeline (Local)

1. **Upload raw data to S3**
   ```bash
   python src/data_ingestion/s3_uploader.py
   ```
   ✅ Should upload 5 CSV files to S3

2. **Process data**
   ```bash
   python src/data_processing/etl_processor.py
   ```
   ✅ Should clean data and create business metrics

3. **Run orchestrated pipeline**
   ```bash
   python src/orchestration/prefect_flows.py
   ```
   ✅ Should show complete pipeline execution

### 🔄 Step 4: Prefect Orchestration

1. **Start Prefect server**
   ```bash
   prefect server start
   ```

2. **Access Prefect UI**
   Open: http://localhost:4200
   ✅ Should show Prefect dashboard

3. **View pipeline execution**
   - See flow runs, tasks, and logs
   - Monitor performance and errors

### 🐳 Step 5: Containerization (Production)

1. **Build and start containers**
   ```bash
   cd "D:\Hands-On-Project"
   docker-compose -f data-pipeline/docker-compose.yml up --build -d
   ```

2. **Run containerized pipeline**
   ```bash
   docker exec -it data-pipeline-data-pipeline-1 python data-pipeline/src/orchestration/prefect_flows.py
   ```

3. **Access containerized Prefect UI**
   Open: http://localhost:4200
   ✅ Should show pipeline execution in containers

## 📊 What You'll Learn

### Module 1: Data Pipeline Fundamentals
- ✅ ETL vs ELT patterns
- ✅ Data lake architecture
- ✅ Batch processing concepts
- ✅ Error handling strategies

### Module 2: Cloud Data Engineering
- ✅ AWS S3 data lake setup
- ✅ IAM permissions and security
- ✅ Data partitioning strategies
- ✅ Cost optimization techniques

### Module 3: Workflow Orchestration
- ✅ Prefect flow design
- ✅ Task dependencies
- ✅ Scheduling and triggers
- ✅ Monitoring and alerting

### Module 4: Production Deployment
- ✅ Docker containerization
- ✅ Multi-service architecture
- ✅ Environment management
- ✅ Scaling strategies

### Module 5: Data Quality & Testing
- ✅ Data validation patterns
- ✅ Unit testing for data pipelines
- ✅ Great Expectations framework
- ✅ Pipeline monitoring


## Sample Data Overview

Your pipeline processes realistic e-commerce data:

| Dataset | Records | Description |
|---------|---------|-------------|
| **customers.csv** | 1,000+ | Customer profiles, demographics |
| **products.csv** | 500+ | Product catalog, categories, pricing |
| **orders.csv** | 2,000+ | Order transactions, timestamps |
| **order_items.csv** | 6,000+ | Individual items per order |
| **reviews.csv** | 1,500+ | Customer reviews and ratings |

## 🔧 Troubleshooting Guide

### Common Issues:

**❌ "AWS credentials not found"**
- Solution: Create `.env` file with valid AWS credentials
- Check: File is in project root, not inside data-pipeline folder

**❌ "Docker daemon not running"**
- Solution: Start Docker Desktop application
- Check: Docker icon in system tray shows running status

**❌ "Can't connect to Prefect server"**
- Solution: Wait 30 seconds after starting containers
- Check: http://localhost:4200 loads properly

**❌ "Python module not found"**
- Solution: Activate virtual environment and reinstall requirements
- Check: `pip list` shows all required packages

## Project Completion

By the end of this course, you'll have built:

✅ **Production-ready data pipeline** processing real e-commerce data  
✅ **Cloud-based data lake** on AWS S3  
✅ **Professional orchestration** with Prefect monitoring  
✅ **Containerized deployment** ready for any environment  
✅ **Comprehensive understanding** of modern data engineering  

## Next Steps & Career Path

After completing this project:

1. **Add to your portfolio** - Showcase on GitHub and LinkedIn
2. **Extend functionality** - Add real-time streaming, machine learning
3. **Learn advanced tools** - Apache Airflow, dbt, Snowflake
4. **Apply for roles** - Data Engineer, Analytics Engineer, Platform Engineer

## Support & Resources

-  **Full Documentation**: See `CONTAINERIZATION_GUIDE.md`
-  **Issues**: Check troubleshooting section above
-  **Questions**: Review code comments and documentation
-  **Best Practices**: Follow the patterns in provided code

---

**🎯 Ready to become a data engineer? Let's build something amazing!** 🚀