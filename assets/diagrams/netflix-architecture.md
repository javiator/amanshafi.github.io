# Netflix Architecture Overview

## High-Level Architecture Diagram

```mermaid
%%{init: {'theme':'base', 'themeVariables': { 'primaryColor':'#E50914','primaryTextColor':'#fff','primaryBorderColor':'#B20710','lineColor':'#666','secondaryColor':'#221f1f','tertiaryColor':'#333','background':'#fff','mainBkg':'#E50914','secondBkg':'#f5f5f5','clusterBkg':'#fafafa','clusterBorder':'#ddd','titleColor':'#333','edgeLabelBackground':'#fff','fontSize':'14px'}}}%%
graph TB
    subgraph clients["🖥️ Client Layer"]
        Web["<b>Web Browsers</b><br/><i>React + Redux</i>"]
        Mobile["<b>Mobile Apps</b><br/><i>iOS & Android</i>"]
        TV["<b>Smart TVs</b><br/><i>Multiple Platforms</i>"]
        Console["<b>Game Consoles</b><br/><i>PS, Xbox, Switch</i>"]
    end

    subgraph edge["☁️ Edge Layer"]
        DNS["<b>Global DNS</b><br/><i>Route Management</i>"]
        CloudFront["<b>CloudFront</b><br/><i>Static Assets & APIs</i>"]
    end

    subgraph gateway["🚪 API Gateway"]
        Zuul["<b>Zuul 2.0</b><br/><i>Async Gateway</i><br/>Rate Limiting"]
    end

    subgraph services["⚙️ Microservices Cluster - AWS"]
        UserService["<b>User Service</b><br/><i>Profiles</i>"]
        AuthService["<b>Auth Service</b><br/><i>OAuth & JWT</i>"]
        RecommendationService["<b>Recommendations</b><br/><i>ML-Powered</i>"]
        SearchService["<b>Search</b><br/><i>Real-time</i>"]
        PlaybackService["<b>Playback</b><br/><i>ABR Streaming</i>"]
        BillingService["<b>Billing</b><br/><i>Subscriptions</i>"]
        ContentService["<b>Content Meta</b><br/><i>Catalog</i>"]
    end

    subgraph storage["💾 Data Storage Layer"]
        Cassandra[("<b>Cassandra</b><br/><i>NoSQL</i><br/>User Data")]
        MySQL[("<b>MySQL</b><br/><i>RDBMS</i><br/>Billing")]
        ElasticSearch[("<b>ElasticSearch</b><br/><i>Search Index</i>")]
        S3[("<b>S3</b><br/><i>Object Store</i><br/>Video")]
        EVCache["<b>EVCache</b><br/><i>In-Memory</i><br/>Cache"]
    end

    subgraph streaming["📺 Streaming Infrastructure"]
        OpenConnect["<b>Open Connect</b><br/><i>Custom CDN</i>"]
        ISP["<b>ISP Locations</b><br/><i>Edge Servers</i>"]
        Encoder["<b>Encoding</b><br/><i>Multi-Quality</i><br/>AV1/H.265"]
    end

    subgraph bigdata["📊 Big Data & ML Pipeline"]
        Kafka["<b>Apache Kafka</b><br/><i>Event Stream</i>"]
        Spark["<b>Apache Spark</b><br/><i>Processing</i>"]
        Hadoop["<b>Data Lake</b><br/><i>S3-based</i>"]
        ML["<b>ML Models</b><br/><i>TensorFlow</i><br/>Personalization"]
    end

    Web -.->|Static| CloudFront
    Mobile -.->|Static| CloudFront
    TV -.->|Static| CloudFront
    Console -.->|Static| CloudFront

    DNS ==>|API Route| Zuul
    DNS ==>|Playback| OpenConnect
    Web -.->|API| Zuul
    Mobile -.->|API| Zuul
    TV -.->|API| Zuul
    Console -.->|API| Zuul
    Web -.->|Video| OpenConnect
    Mobile -.->|Video| OpenConnect
    TV -.->|Video| OpenConnect
    Console -.->|Video| OpenConnect

    Zuul ==>|HTTPS| UserService
    Zuul ==>|HTTPS| AuthService
    Zuul ==>|HTTPS| RecommendationService
    Zuul ==>|HTTPS| SearchService
    Zuul ==>|HTTPS| PlaybackService
    Zuul ==>|HTTPS| BillingService
    Zuul ==>|HTTPS| ContentService

    UserService -->|Query| Cassandra
    UserService -->|Cache| EVCache
    AuthService -->|Verify| Cassandra
    RecommendationService -->|Read| EVCache
    RecommendationService -->|Predict| ML
    SearchService -->|Index| ElasticSearch
    BillingService -->|ACID| MySQL
    ContentService -->|Meta| Cassandra

    PlaybackService ==>|Stream| OpenConnect
    OpenConnect ==>|Deliver| ISP
    S3 -->|Source| Encoder
    Encoder ==>|Push| OpenConnect

    UserService -.->|Events| Kafka
    PlaybackService -.->|Telemetry| Kafka
    RecommendationService -.->|Metrics| Kafka
    Kafka ==>|Process| Spark
    Spark -->|Store| Hadoop
    Spark ==>|Train| ML
    ML ==>|Serve| RecommendationService

    classDef clientStyle fill:#E50914,stroke:#B20710,stroke-width:3px,color:#fff,rx:10,ry:10
    classDef edgeStyle fill:#333,stroke:#666,stroke-width:2px,color:#fff,rx:10,ry:10
    classDef serviceStyle fill:#0071eb,stroke:#005bb5,stroke-width:2px,color:#fff,rx:10,ry:10
    classDef storageStyle fill:#16a34a,stroke:#15803d,stroke-width:2px,color:#fff,rx:10,ry:10
    classDef streamStyle fill:#7c3aed,stroke:#6d28d9,stroke-width:2px,color:#fff,rx:10,ry:10
    classDef dataStyle fill:#f59e0b,stroke:#d97706,stroke-width:2px,color:#fff,rx:10,ry:10

    class Web,Mobile,TV,Console clientStyle
    class DNS,CloudFront,Zuul edgeStyle
    class UserService,AuthService,RecommendationService,SearchService,PlaybackService,BillingService,ContentService serviceStyle
    class Cassandra,MySQL,ElasticSearch,S3,EVCache storageStyle
    class OpenConnect,ISP,Encoder streamStyle
    class Kafka,Spark,Hadoop,ML dataStyle
```

## Detailed Component Architecture

```mermaid
%%{init: {'theme':'base', 'themeVariables': { 'primaryColor':'#E50914','primaryTextColor':'#fff','primaryBorderColor':'#B20710','lineColor':'#666','fontSize':'14px'}}}%%
graph LR
    subgraph resilience["🛡️ Resilience & Traffic Control"]
        ConcurrencyLimits["<b>Adaptive Concurrency</b><br/><i>Load Shedding</i><br/>Concurrency Limits"]
        ServiceMesh["<b>Service Mesh</b><br/><i>Envoy/Prana</i><br/>Traffic Shaping"]
        Eureka["<b>Service Registry</b><br/><i>Eureka</i><br/>Discovery"]
    end

    subgraph observability["📈 Observability Stack"]
        Atlas["<b>Atlas</b><br/><i>Metrics</i><br/>Time-series DB"]
        Mantis["<b>Mantis</b><br/><i>Stream Processing</i><br/>Real-time Analytics"]
        Trace["<b>Distributed Tracing</b><br/><i>Request Tracking</i><br/>Latency Analysis"]
    end

    subgraph deployment["🚀 Deployment Pipeline"]
        Spinnaker["<b>Spinnaker</b><br/><i>CD Platform</i><br/>Multi-cloud"]
        Titus["<b>Titus</b><br/><i>Container Mgmt</i><br/>EC2 Orchestration"]
        Chaos["<b>Chaos Engineering</b><br/><i>Chaos Monkey & ChAP</i><br/>Resilience Testing"]
    end

    Eureka ==>|Discovery| ServiceMesh
    ServiceMesh ==>|Policies| ConcurrencyLimits
    ConcurrencyLimits -.->|Signals| Atlas
    Atlas ==>|Streams| Mantis
    Trace -.->|Feeds| Mantis

    Spinnaker ==>|Deploys| Titus
    Chaos -.->|Tests| Titus
    Titus -.->|Metrics| Atlas

    classDef resilienceStyle fill:#dc2626,stroke:#991b1b,stroke-width:2px,color:#fff,rx:10,ry:10
    classDef observeStyle fill:#8b5cf6,stroke:#6d28d9,stroke-width:2px,color:#fff,rx:10,ry:10
    classDef deployStyle fill:#059669,stroke:#047857,stroke-width:2px,color:#fff,rx:10,ry:10

    class ConcurrencyLimits,ServiceMesh,Eureka resilienceStyle
    class Atlas,Mantis,Trace observeStyle
    class Spinnaker,Titus,Chaos deployStyle
```

## Architecture Description

### Client Layer
Netflix supports multiple platforms including web browsers, mobile apps (iOS/Android), smart TVs, gaming consoles, and streaming devices. Each client is optimized for its platform while maintaining consistent user experience.

### Edge Layer
**Open Connect** appliances positioned inside partner ISPs carry the bulk of video delivery, while **global DNS** steers devices to the closest healthy edge. **AWS CloudFront** augments this for static assets, images, and some API acceleration rather than serving primary streaming traffic.

### API Gateway
**Zuul** acts as the front door for all requests, handling dynamic routing, monitoring, security, and resilience. It routes requests to appropriate microservices and applies cross-cutting concerns like authentication, rate limiting, and request filtering.

### Microservices Architecture
Netflix pioneered microservices at scale with hundreds of services:
- **User Service**: Manages profiles, preferences, and viewing history
- **Authentication Service**: Handles login, session management, and security
- **Recommendation Engine**: Powers personalized content suggestions using machine learning
- **Search Service**: Provides fast, relevant content discovery
- **Playback Service**: Manages streaming sessions and quality adaptation
- **Billing Service**: Handles subscriptions and payments
- **Content Metadata Service**: Stores information about movies, shows, and episodes

### Data Storage
Netflix uses **polyglot persistence**:
- **Cassandra**: Primary NoSQL database for user data, viewing history, and distributed data requiring high availability
- **MySQL**: Transactional data like billing and subscriptions
- **ElasticSearch**: Powers search functionality with full-text indexing
- **S3**: Stores encoded video content, images, and backups
- **EVCache**: Distributed memcached-based caching layer for performance

### Streaming Infrastructure
**Open Connect** is Netflix's primary CDN with appliances placed in ISP data centers worldwide. Video encoding creates multiple quality versions (4K to mobile) using adaptive bitrate streaming, and content is pre-positioned near users for optimal performance.

### Big Data Pipeline
- **Apache Kafka**: Real-time event streaming for user interactions, playback events, and system metrics
- **Apache Spark**: Batch and stream processing for analytics
- **Hadoop/S3**: Data lake for historical analysis
- **Machine Learning**: Powers recommendations, artwork personalization, encoding optimization, and quality of experience

### Resilience & Reliability
Netflix now emphasizes adaptive protection layers:
- **Adaptive Concurrency Limits**: Load shedding and backpressure replacing legacy Hystrix patterns
- **Service Mesh Policies**: Envoy/Prana filters handle retries, timeouts, and regional failover
- **Service Registry (Eureka)**: Dynamic discovery for hundreds of services
- **Chaos Engineering**: Chaos Monkey and ChAP continuously validate failure tolerance

### Observability
- **Atlas**: Time-series monitoring for metrics across all services
- **Mantis**: Real-time stream processing for operational insights
- **Distributed Tracing**: Tracks requests across microservices

### Deployment
- **Spinnaker**: Multi-cloud continuous delivery platform for safe deployments
- **Titus**: Container management platform orchestrating workloads on Amazon EC2

### Key Characteristics
1. **Global Scale**: Serves 200+ million subscribers across 190+ countries
2. **Cloud-Native**: Runs primarily on AWS with multi-region architecture, complemented by Netflix-owned Open Connect infrastructure
3. **Microservices**: Hundreds of loosely coupled services
4. **API-First**: All functionality exposed through well-defined APIs
5. **Data-Driven**: Every decision backed by A/B testing and analytics
6. **Resilient**: Built to handle failures gracefully with chaos engineering

This architecture enables Netflix to stream billions of hours of content monthly while maintaining high availability and delivering personalized experiences at massive scale.
