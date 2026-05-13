import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zenelait_infotech.settings')
django.setup()

from django.contrib.auth.models import User
from services.models import Service
from blog.models import Category, Post
from careers.models import JobListing
from core.models import Testimonial

def load_sample():
    print("Clearing old objects...")
    Service.objects.all().delete()
    Category.objects.all().delete()
    JobListing.objects.all().delete()
    Testimonial.objects.all().delete()

    admin_user = User.objects.first()
    if not admin_user:
        # Ensure an admin user exists for ForeignKey
        admin_user = User.objects.create_superuser('admin', 'admin@zenelait.com', 'adminpass')
        print("Created admin superuser.")

    # 7 Product-oriented Corporate Services
    services_data = [
        {
            "title": "Customer Relationship Management",
            "icon_class": "fas fa-users-cog",
            "short_description": "Our flagship Cloud CRM Platform enables intelligent client life-cycle tracking and high-throughput funnel automations.",
            "detailed_description": "Zenelait CRM is a robust enterprise software product built to streamline customer insights. Features include pipeline visualization, automated follow-ups, dynamic API integrations, and real-time business intelligence dashboards designed for growth-focused sales ecosystems."
        },
        {
            "title": "Enterprise Resource Planning",
            "icon_class": "fas fa-sitemap",
            "short_description": "A unified Cloud ERP Ecosystem consolidating core workflows from supply chains to treasury management into a modular workspace.",
            "detailed_description": "Our Enterprise Resource Planning suite represents the pinnacle of integrated SaaS engineering. Scale with comprehensive supply chain nodes, modular ledger systems, HR tracking components, and live telemetry engines capable of absorbing global organizational data streams."
        },
        {
            "title": "Learning Management System",
            "icon_class": "fas fa-graduation-cap",
            "short_description": "A feature-rich digital LMS delivering secure knowledge pipelines, course hosting engines, and cognitive analytics tools.",
            "detailed_description": "The Zenelait LMS delivers a resilient cloud-native infrastructure for enterprise workforce development and academic verticals. Benefit from low-latency video streams, gamified lesson matrices, responsive test portals, and robust grading algorithms."
        },
        {
            "title": "Billing Software",
            "icon_class": "fas fa-file-invoice-dollar",
            "short_description": "A fully compliant Billing and Recurring Revenue Engine automating invoicing, dynamic taxation, and secure payment handshakes.",
            "detailed_description": "Engineered for optimal financial integrity, our Billing Software automates high-volume transactions. Equipped with multi-currency calculators, automated renewal logic, PDF reporting engines, and enterprise-grade encryption protecting critical payment data."
        },
        {
            "title": "Website Development",
            "icon_class": "fas fa-code",
            "short_description": "Bespoke, highly responsive corporate channels optimized for high core web vitals metrics and secure payload serving.",
            "detailed_description": "From architectural mapping to serverless deployment, our Website Development unit engineers lightning-fast user interfaces using React and high-performance Django pipelines. Gain seamless cross-platform responsiveness, strict search-engine optimizations, and fluid user experience frameworks."
        },
        {
            "title": "IT Consulting",
            "icon_class": "fas fa-network-wired",
            "short_description": "Comprehensive technology advisory mapping robust migration paths and designing scalable, zero-trust cloud infrastructures.",
            "detailed_description": "Leverage Zenelait advisory pipelines to map scalable architectures, secure network perimeters, and select efficient technology stacks. We offer in-depth infrastructure audits and transition guides that de-risk cloud and on-prem structural overhauls."
        },
        {
            "title": "Software Consulting",
            "icon_class": "fas fa-laptop-medical",
            "short_description": "Strategic architectural engineering and code audits to scale performance envelopes and maximize software ROI yields.",
            "detailed_description": "We bridge complex technical bottlenecks by conducting granular audits of monolithic codebases and optimizing application logic for modern concurrency. From microservices migrations to containerized orchestrations, we ensure application resilience."
        }
    ]

    print("Inserting 7 custom services...")
    for sd in services_data:
        Service.objects.create(**sd)
    print("Successfully inserted all services.")

    # Sample Blog
    c1 = Category.objects.create(name="SaaS Engineering")
    c2 = Category.objects.create(name="Fintech Infrastructure")

    Post.objects.create(
        title="Architecting Multi-Tenant SaaS Ecosystems for scale",
        author=admin_user,
        category=c1,
        summary="Exploring data-isolation patterns and container orchestration loops powering modern CRM and ERP solutions.",
        content="Scaling product ecosystems necessitates highly resilient tenancy architectures. At Zenelait, our core ERP utilizes advanced database partitioning and micro-service gateways, delivering isolated nodes to our global clients and maximizing isolation velocity...",
        is_published=True
    )
    print("Inserted Blog data.")

    # Careers
    JobListing.objects.create(
        title="Senior SaaS Platform Engineer",
        department="Core R&D",
        location="Chennai, India",
        job_type="FT",
        description="Scale core multi-tenant CRM APIs.",
        requirements="Python, Django REST Framework, PostgreSQL, Kubernetes."
    )
    JobListing.objects.create(
        title="Lead Product Designer",
        department="UI/UX Lab",
        location="Remote / Hybrid",
        job_type="FT",
        description="Design the next gen interfaces for our Billing and LMS platforms.",
        requirements="Figma, Webflow, HTML/CSS prototyping, interaction animations."
    )
    print("Inserted Jobs.")

    # Testimonial
    Testimonial.objects.create(
        client_name="Marcus Avery",
        designation="Director of Platforms",
        company="AeroTech Global",
        content="Migrating to Zenelait's ERP and Invoicing systems completely consolidated our logistics footprint. Their product interfaces are intuitively fast and engineered perfectly for high load."
    )
    print("Initial Load Successful.")

if __name__ == "__main__":
    load_sample()
