import React, { useEffect, useState } from 'react';
import { Shield, Server, Users, AlertTriangle, CheckCircle, Clock, Database, Cloud } from 'lucide-react';

const phases = [
  { id: 1, name: 'Assessment & Escopo', status: 'Concluído', progress: 100, icon: <Database size={24} /> },
  { id: 2, name: 'Design & Governança', status: 'Concluído', progress: 100, icon: <Shield size={24} /> },
  { id: 3, name: 'Operação AWS & Treinamento', status: 'Em Andamento', progress: 30, icon: <Server size={24} />, active: true },
  { id: 4, name: 'Avaliação de Prontidão', status: 'Pendente', progress: 0, icon: <CheckCircle size={24} /> },
  { id: 5, name: 'Certificação Oficial', status: 'Pendente', progress: 0, icon: <Cloud size={24} /> }
];

const gaps = [
  {
    id: 'GAP-001/002/003',
    title: 'SecOps: Hardening AWS',
    desc: 'Ligar serviço GuardDuty, forçar autenticação MFA na conta Root AWS e rotacionar a chave IAM antiga do usuário tmpsaasboost.',
    status: 'Blocker',
    owner: 'Equipe DevOps',
    icon: <AlertTriangle size={20} />
  },
  {
    id: 'GAP-004',
    title: 'Teste de Disaster Recovery',
    desc: 'Rodar o roteiro de restore do banco de dados (RDS) em ambiente sandbox para validar o RTO/RPO e gerar o laudo de evidência (BCP).',
    status: 'Blocker',
    owner: 'Equipe DevOps',
    icon: <Server size={20} />
  },
  {
    id: 'TRAIN-001',
    title: 'Treinamento de Conscientização',
    desc: 'Matricular todos os 10 funcionários em plataforma de Security Awareness e LGPD, coletando certificados de conclusão.',
    status: 'In Progress',
    owner: 'RH / Diretoria',
    icon: <Users size={20} />
  }
];

function App() {
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    setMounted(true);
  }, []);

  return (
    <div className="dashboard-container">
      {/* Header */}
      <header className="header animate-fade-in">
        <div>
          <h1>TWYN ISMS Dashboard</h1>
          <p style={{ color: 'var(--text-secondary)', marginTop: '0.5rem', fontWeight: 300, letterSpacing: '1px' }}>ISO/IEC 27001:2022 Certification Journey</p>
        </div>
        <div className="header-meta">
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            <Clock size={16} /> Updated: June 2026
          </div>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            <Shield size={16} /> Fast Track Model
          </div>
        </div>
      </header>

      {/* Phases Progress */}
      <div style={{ marginBottom: '2rem' }}>
        <h2 className="section-title animate-fade-in delay-1">Project Phases</h2>
        <div className="phases-grid">
          {phases.map((phase, index) => (
            <div key={phase.id} className={`glass-card phase-card animate-fade-in`} style={{ animationDelay: `${0.1 * index}s`}}>
              <div style={{ color: 'var(--text-primary)', opacity: phase.active ? 1 : 0.5, marginBottom: '1rem', display: 'flex', justifyContent: 'center' }}>
                {phase.icon}
              </div>
              <h3 className="phase-title">Fase {phase.id}</h3>
              <p style={{ fontSize: '0.9rem', marginBottom: '0.5rem', color: 'var(--text-secondary)' }}>{phase.name}</p>
              <div className="phase-status">{phase.status}</div>
              
              <div className="progress-bar-container">
                <div 
                  className={`progress-bar ${phase.progress === 100 ? 'progress-done' : (phase.active ? 'progress-active' : '')}`}
                  style={{ width: mounted ? `${phase.progress}%` : '0%' }}
                ></div>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Active Gaps Tracker */}
      <div>
        <h2 className="section-title animate-fade-in delay-2">Active Technical Blockers (Fase 3)</h2>
        <div className="gaps-grid">
          {gaps.map((gap, index) => (
            <div key={gap.id} className="glass-card gap-card animate-fade-in" style={{ animationDelay: `${0.2 + (0.1 * index)}s`}}>
              <div className="gap-header">
                <span style={{ fontSize: '0.85rem', color: 'var(--text-secondary)', fontFamily: 'monospace' }}>{gap.id}</span>
                <span className={`badge ${gap.status === 'Blocker' ? 'blocker' : 'in-progress'}`}>
                  {gap.status}
                </span>
              </div>
              <h3 className="gap-title">{gap.title}</h3>
              <p className="gap-desc">{gap.desc}</p>
              <div className="gap-owner">
                {gap.icon} {gap.owner}
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Data Room Stats */}
      <footer className="data-room animate-fade-in delay-3">
        <div>
          <h3 style={{ fontSize: '1.2rem', marginBottom: '0.5rem' }}>Data Room & Governança</h3>
          <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem' }}>Base documental higienizada no GitHub. Pronta para Auditoria Fase 1.</p>
        </div>
        <div className="data-room-stats">
          <div className="stat-item">
            <span className="stat-value" style={{ color: 'var(--status-success)' }}>100%</span>
            <span className="stat-label">Políticas Aprovadas</span>
          </div>
          <div className="stat-item">
            <span className="stat-value" style={{ color: 'var(--status-info)' }}>12+</span>
            <span className="stat-label">Evidências Prontas</span>
          </div>
          <div className="stat-item">
            <span className="stat-value" style={{ color: 'var(--status-warning)' }}>3</span>
            <span className="stat-label">Evidências Pendentes</span>
          </div>
        </div>
      </footer>
    </div>
  );
}

export default App;
