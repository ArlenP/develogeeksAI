# AgentOS

AgentOS es un sistema de agentes de IA construido desde cero con Python y Arquitectura Hexagonal.

El objetivo del proyecto no es crear un chatbot, sino una plataforma donde múltiples agentes especializados colaboren para resolver tareas complejas de manera modular, escalable y mantenible.

Este proyecto también sirve como laboratorio para aprender Ingeniería de Software aplicada a Inteligencia Artificial, cubriendo patrones de diseño, arquitectura, LLMs, herramientas (Tools), memoria y sistemas multiagente.

---

# Objetivos

- Construir un sistema multiagente desde cero.
- Aprender Arquitectura Hexagonal aplicada a IA.
- Implementar patrones de diseño reales.
- Integrar distintos proveedores de LLM.
- Diseñar agentes reutilizables.
- Crear una plataforma extensible para futuros proyectos.

---

# Visión

En lugar de un único asistente inteligente, AgentOS está compuesto por varios agentes especializados.

```
                +------------------+
                |      User        |
                +------------------+
                          |
                          |
                    AgentOS Core
                          |
      ------------------------------------------
      |          |          |          |        |
 BlogAgent   MobileDev  Architecture Daily   ...
              Agent        Agent     Assistant
```

Cada agente conoce un dominio específico y puede colaborar con otros agentes cuando una tarea lo requiera.

---

# Agentes iniciales

## BlogAgent

Especializado en creación de contenido técnico.

Responsabilidades:

- Generar ideas de artículos
- Crear estructuras de posts
- Explicar conceptos técnicos
- SEO técnico básico
- Adaptar contenido a distintas audiencias

---

## ArchitectureAgent

Especializado en arquitectura de software.

Responsabilidades:

- System Design
- Arquitectura Hexagonal
- Clean Architecture
- Patrones de diseño
- Arquitecturas distribuidas
- Staff Engineer Thinking

---

## MobileDevAgent

Especializado en desarrollo móvil.

Responsabilidades:

- Swift
- SwiftUI
- UIKit
- Kotlin Multiplatform
- Arquitectura iOS
- Patrones de UI
- Performance

---

## DailyAssistantAgent

Asistente para productividad diaria.

Responsabilidades:

- Resúmenes
- Organización de tareas
- Debugging
- Explicación de errores
- Generación de snippets
- Automatización de pequeñas tareas

---

# Arquitectura

El proyecto sigue una Arquitectura Hexagonal (Ports & Adapters).

```
                +------------------+
                |    Application   |
                +------------------+
                         |
                 +---------------+
                 |     Core      |
                 +---------------+
                /       |        \
      Ports   Agents   Domain   Models
                \
          Infrastructure
```

Los agentes dependen únicamente de interfaces (Ports), nunca de implementaciones concretas.

---

# Stack

- Python 3.12+
- Arquitectura Hexagonal
- Dependency Injection
- LLM Providers
- Ollama
- OpenAI
- Anthropic
- Google Gemini
- Pytest

---

# Roadmap

## Sprint 1

- Arquitectura Hexagonal
- BaseAgent
- Interfaces
- FakeLLMClient

## Sprint 2

- Dependency Injection
- Container
- Composition Root

## Sprint 3

- Adapter Pattern
- LLM Providers

## Sprint 4

- Tool Registry

## Sprint 5

- Memory

## Sprint 6

- Multi-Agent Communication

## Sprint 7

- RAG

## Sprint 8

- Workflows

## Sprint 9

- API

## Sprint 10

- Web Interface

---

# Estructura del proyecto

```
src/
│
├── application/
│
├── core/
│   ├── agents/
│   ├── ports/
│   ├── models/
│   └── services/
│
├── infrastructure/
│   ├── llm/
│   ├── memory/
│   ├── tools/
│   └── persistence/
│
└── main.py
```

---

# Filosofía

AgentOS prioriza:

- Bajo acoplamiento
- Alta cohesión
- Componentes intercambiables
- Código testeable
- Escalabilidad
- Aprendizaje continuo

Cada decisión de diseño busca acercar el proyecto a una plataforma profesional de agentes de IA.
