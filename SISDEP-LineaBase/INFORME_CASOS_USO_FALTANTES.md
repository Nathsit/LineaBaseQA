# Informe de Casos de Uso Faltantes - SISDEP
## Plan de Implementación y Despliegue

**Fecha**: 2025-01-XX  
**Proyecto**: SISDEP - Migración a Playwright con Python  
**Objetivo**: Completar casos de uso faltantes e implementar CI/CD en Azure DevOps

---

## 📊 Resumen Ejecutivo

| Métrica | Valor |
|---------|-------|
| **Total de casos de uso** | 62 |
| **Casos implementados** | 36 |
| **Casos faltantes** | 26 |
| **Porcentaje completado** | **58.1%** |
| **Tiempo total estimado** | **2 semanas (80 horas)** |
| **Tiempo para casos de uso** | **7 días (56 horas)** |
| **Tiempo para CI/CD y despliegue** | **3 días (24 horas)** |

---

## ❌ CASOS DE USO FALTANTES (26)

### Regulaciones - Autorizaciones (7 casos)
1. ❌ **Actualizar una visita administrativa** (14)
2. ❌ **Actualizar una resolución** (16)
3. ❌ **Registrar la entrega de un módulo en una autorización** (17)
4. ❌ **Agregar un recurso a la resolución** (18)
5. ❌ **Agregar una notificación a la resolución** (19)
6. ❌ **Agregar seguimiento a la notificación** (20)
7. ❌ **Actualizar la información general de una autorización** (21)

### Regulaciones - Visitas (1 caso)
8. ❌ **Generar reporte Excel de visitas domiciliarias** (25)

### Regulaciones - Módulos (2 casos)
9. ❌ **Generar reporte Excel de módulos** (30)
10. ❌ **Eliminar un módulo (en uso)** (59)

### Social - Estudio Socioeconómico (3 casos)
11. ❌ **Actualizar un estudio socioeconómico** (36)
12. ❌ **Generar PDF del Concepto socioeconómico** (39)
13. ❌ **Firmar un estudio socioeconómico (incompleto)** (60)

### Social - Ofertas Institucionales (5 casos)
14. ❌ **Actualizar una oferta institucional** (41)
15. ❌ **Actualizar la información de un participante** (44)
16. ❌ **Registrar evidencia a una oferta** (46)
17. ❌ **Generar reporte Excel de ofertas institucionales** (47)
18. ❌ **Generar reporte Excel de los participantes de una oferta** (48)

### Social - Vehículos (1 caso)
19. ❌ **Actualizar un vehículo** (50)

### Casos Negativos Adicionales (1 caso)
20. ❌ **Registrar la entrega de un módulo (archivos faltantes)** (58)

---

## ⏱️ Plan de Implementación (2 Semanas - 80 horas)

### 📅 Semana 1 (40 horas)

#### Días 1-2 (16 horas) - Alta Prioridad
**Objetivo**: Completar 5 casos críticos de actualización

| # | Caso de Uso | Tiempo | Prioridad |
|---|-------------|--------|-----------|
| 1 | Actualizar una visita administrativa | 2-3h | 🔴 Alta |
| 2 | Actualizar una resolución | 2-3h | 🔴 Alta |
| 3 | Actualizar la información general de una autorización | 2-3h | 🔴 Alta |
| 4 | Actualizar un vehículo | 1.5-2h | 🔴 Alta |
| 5 | Actualizar una oferta institucional | 2-3h | 🔴 Alta |

**Total**: 12-15 horas

#### Días 3-4 (16 horas) - Media Prioridad
**Objetivo**: Completar reportes Excel y actualizaciones importantes

| # | Caso de Uso | Tiempo | Prioridad |
|---|-------------|--------|-----------|
| 6 | Generar reporte Excel de visitas domiciliarias | 2.5-3h | 🟡 Media |
| 7 | Generar reporte Excel de módulos | 2.5-3h | 🟡 Media |
| 8 | Generar reporte Excel de ofertas institucionales | 2.5-3h | 🟡 Media |
| 9 | Actualizar un estudio socioeconómico | 3-4h | 🟡 Media |
| 10 | Actualizar la información de un participante | 2-3h | 🟡 Media |

**Total**: 15-18 horas

#### Día 5 (8 horas) - Baja Prioridad (Inicio)
**Objetivo**: Iniciar casos de baja prioridad

| # | Caso de Uso | Tiempo | Prioridad |
|---|-------------|--------|-----------|
| 11 | Eliminar un módulo (en uso) | 1h | 🟢 Baja |
| 12 | Generar PDF del Concepto socioeconómico | 2-2.5h | 🟢 Baja |
| 13 | Firmar un estudio socioeconómico (incompleto) | 1.5-2h | 🟢 Baja |
| 14 | Registrar evidencia a una oferta | 1.5-2h | 🟢 Baja |
| 15 | Generar reporte Excel de los participantes de una oferta | 2-2.5h | 🟢 Baja |

**Total**: 8-10 horas

**Resumen Semana 1**: 35-43 horas de casos de uso

---

### 📅 Semana 2 (40 horas)

#### Días 1-2 (16 horas) - Baja Prioridad (Continuación)
**Objetivo**: Completar casos restantes de baja prioridad

| # | Caso de Uso | Tiempo | Prioridad |
|---|-------------|--------|-----------|
| 16 | Registrar la entrega de un módulo en una autorización | 1.5-2h | 🟢 Baja |
| 17 | Agregar un recurso a la resolución | 1.5-2h | 🟢 Baja |
| 18 | Agregar una notificación a la resolución | 1.5-2h | 🟢 Baja |
| 19 | Agregar seguimiento a la notificación | 1.5-2h | 🟢 Baja |
| 20 | Registrar la entrega de un módulo (archivos faltantes) | 1.5-2h | 🟢 Baja |
| 21-26 | Casos adicionales de autorizaciones | 8-10h | 🟢 Baja |

**Total**: 15-20 horas

**Resumen casos de uso**: 50-63 horas (7 días)

#### Días 3-5 (24 horas) - CI/CD y Despliegue en Azure DevOps
**Objetivo**: Configurar pipelines, despliegues y automatización completa

##### Día 3 (8 horas) - Setup Inicial Azure DevOps
- **Configuración de proyecto Azure DevOps**: 1 hora
  - Crear proyecto/organización
  - Configurar repositorio
  - Permisos y seguridad
  
- **Pipeline básico YAML**: 3 horas
  - Estructura básica del pipeline
  - Configuración de triggers
  - Ejecución de tests básicos
  
- **Configuración de agentes**: 2 horas
  - Self-hosted agents o Microsoft-hosted
  - Configuración de variables de entorno
  
- **Integración con repositorio**: 2 horas
  - Conectar con GitHub/Git
  - Configurar webhooks
  - Pruebas de integración

##### Día 4 (8 horas) - Pipelines Avanzados
- **Pipeline por feature**: 3 horas
  - Pipeline para autenticación
  - Pipeline para administración
  - Pipeline para regulaciones
  - Pipeline para social
  
- **Pipeline de reportes**: 2 horas
  - Generación automática de reportes HTML
  - Reportes por feature
  - Almacenamiento de artefactos
  
- **Pipeline de validación**: 2 horas
  - Validación de código
  - Linting
  - Tests de calidad
  
- **Notificaciones y alertas**: 1 hora
  - Configurar notificaciones de fallos
  - Integración con Teams/Email

##### Día 5 (8 horas) - Despliegue y Documentación
- **Configuración de entornos**: 2 horas
  - Ambiente de desarrollo
  - Ambiente de staging
  - Ambiente de producción
  
- **Scripts de despliegue**: 3 horas
  - Automatización de despliegues
  - Rollback automático
  - Validación post-despliegue
  
- **Documentación**: 2 horas
  - Documentar pipelines
  - Guía de uso
  - Troubleshooting
  
- **Pruebas finales**: 1 hora
  - Ejecutar pipeline completo
  - Validar despliegue
  - Ajustes finales

---

## 📊 Distribución de Tiempo

| Actividad | Tiempo | % del Total | Días |
|-----------|--------|-------------|------|
| **Casos de Uso - Alta Prioridad** | 12-15 horas | 15-19% | Semana 1, Días 1-2 |
| **Casos de Uso - Media Prioridad** | 15-18 horas | 19-23% | Semana 1, Días 3-4 |
| **Casos de Uso - Baja Prioridad** | 23-30 horas | 29-38% | Semana 1, Día 5 + Semana 2, Días 1-2 |
| **CI/CD y Despliegue Azure DevOps** | 24 horas | 30% | Semana 2, Días 3-5 |
| **Buffer/Contingencia** | 0-8 horas | 0-10% | Distribuido |
| **TOTAL** | **80 horas** | **100%** | **10 días (2 semanas)** |

---

## 🎯 Entregables

### Al Finalizar Semana 1
- ✅ 10-15 casos de uso implementados (Alta y Media Prioridad)
- ✅ Inicio de casos de Baja Prioridad

### Al Finalizar Semana 2
- ✅ **26 casos de uso implementados y probados**
- ✅ **Pipeline CI/CD en Azure DevOps funcionando**
- ✅ **Pipelines por feature configurados**
- ✅ **Sistema de reportes automatizados**
- ✅ **Scripts de despliegue automatizado**
- ✅ **Configuración de entornos (dev/staging/prod)**
- ✅ **Documentación completa de pipelines**

---

## 🚀 Estrategias de Optimización

### Para Casos de Uso
1. **Reutilización de código**: Aprovechar Page Objects y helpers existentes
2. **Agrupación por funcionalidad**: Implementar casos relacionados juntos
3. **Templates**: Crear templates para casos similares (reportes, actualizaciones)
4. **Paralelización**: Casos independientes pueden desarrollarse en paralelo

### Para CI/CD
1. **Templates de pipeline**: Reutilizar estructuras YAML base
2. **Variables compartidas**: Centralizar configuración
3. **Artefactos compartidos**: Optimizar almacenamiento de reportes
4. **Caché de dependencias**: Acelerar builds

---

## ⚠️ Riesgos y Mitigaciones

| Riesgo | Impacto | Mitigación |
|--------|--------|------------|
| Reportes Excel requieren más tiempo | Medio | Priorizar funcionalidad básica, optimizar después |
| Problemas con descargas de archivos | Medio | Usar mocks en desarrollo, validar en staging |
| Configuración compleja de Azure DevOps | Alto | Usar documentación oficial, consultar ejemplos |
| Tiempo insuficiente para todos los casos | Alto | Priorizar Alta y Media, documentar Baja para futuro |
| Problemas de conectividad con Azure | Medio | Tener plan B con ejecución local |

---

## 📈 Métricas de Progreso

### Hitos Semana 1
- **Día 2**: ✅ Completar Alta Prioridad (5 casos)
- **Día 4**: ✅ Completar Media Prioridad (5 casos)
- **Día 5**: ✅ Iniciar Baja Prioridad (5 casos)

### Hitos Semana 2
- **Día 2**: ✅ Completar Baja Prioridad (16 casos) - **Total casos: 26/26**
- **Día 3**: ✅ Setup básico Azure DevOps
- **Día 4**: ✅ Pipelines avanzados funcionando
- **Día 5**: ✅ Despliegue completo y documentado

---

## 📝 Notas Adicionales

- Los tiempos están optimizados asumiendo reutilización de código existente
- Los casos de "Actualizar" comparten estructura similar, acelerando desarrollo
- Los reportes Excel pueden agruparse para optimizar tiempo
- Azure DevOps requiere configuración inicial que puede variar según permisos
- Se recomienda tener acceso de administrador a Azure DevOps para agilizar setup

---

**Preparado por**: Equipo de Automatización SISDEP  
**Última actualización**: 2025-01-XX

