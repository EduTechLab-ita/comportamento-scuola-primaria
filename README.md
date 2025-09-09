# 🎯 Generatore Valutazioni Comportamento Scuola Primaria

[![PWA Ready](https://img.shields.io/badge/PWA-Ready-brightgreen.svg)](https://developer.mozilla.org/docs/Web/Progressive_web_apps)
[![Installable](https://img.shields.io/badge/Installabile-App%20Mobile-blue.svg)](#installazione-pwa)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Applicazione web progressive (PWA) standalone per la **valutazione del comportamento nella scuola primaria**. Calcola automaticamente voti e livelli descrittivi secondo le normative ministeriali, gestisce medie ponderate per lo scrutinio e include funzioni avanzate di import/export dati.

## ✨ Caratteristiche Principali

### 🎯 **Valutazione Comportamento**
- **Calcolo automatico** di voti e livelli descrittivi
- **6 livelli di valutazione**: Ottimo, Distinto, Buono, Discreto, Sufficiente, Non Sufficiente
- **Personalizzazione indicatori** comportamentali
- **Sistema di pesi** per diversi ambiti comportamentali
- **Note personalizzate** per ogni studente

### 📊 **Gestione Dati**
- **Import studenti** da file Excel/CSV
- **Export risultati** in PDF e Excel
- **Backup automatico** dei dati nel browser
- **Ripristino dati** da backup precedenti
- **Stampa ottimizzata** per documenti ufficiali

### 🔧 **Funzionalità Avanzate**
- **Interface responsive** per desktop, tablet e mobile
- **PWA installabile** come app mobile
- **Funziona offline** una volta installata
- **Modalità stampa** ottimizzata per documenti ufficiali
- **Sistema di aiuto integrato** accessibile dal pulsante "?"

## 🚀 Avvio Rapido

### 1. **Apertura Immediata**
```
1. Apri index.html nel browser
2. L'app si carica istantaneamente
3. Inizia subito a usare tutte le funzioni
```

### 2. **Installazione PWA** 
```
📱 Su Mobile (Chrome/Safari):
1. Apri l'app nel browser
2. Tocca il menu → "Aggiungi alla schermata home"
3. L'icona dell'app apparirà sulla home

💻 Su Desktop (Chrome):
1. Apri l'app nel browser
2. Cerca l'icona "Installa" nella barra indirizzi
3. Clicca "Installa" per averla come app desktop
```

## 🎓 Guida Utilizzo Completa

### **Primo Avvio**

1. **Configura Informazioni Scuola**
   - Clicca su "Informazioni scuola" nell'header
   - Inserisci: Istituto, Plesso, Anno Scolastico, Classe
   - Seleziona il coordinatore di classe
   - Salva le impostazioni

2. **Importa Studenti**
   ```
   Metodo 1 - File Excel:
   • Carica file .xlsx con colonna "Nome" o "Studente"
   • L'app rileva automaticamente gli studenti
   
   Metodo 2 - Inserimento Manuale:
   • Usa il campo "Inserimento rapido studenti"
   • Un nome per riga o separati da virgola
   
   Metodo 3 - Copia/Incolla:
   • Copia da registro elettronico
   • Incolla nel campo dedicato
   ```

### **Inserimento Episodi Comportamentali**

1. **Configura Indicatori**
   - L'app include indicatori standard ministeriali
   - Puoi personalizzare pesi e descrizioni
   - Aggiungi indicatori specifici se necessario

2. **Valuta Studenti**
   ```
   Per ogni studente:
   • Seleziona livello per ogni indicatore (Ottimo → Non Sufficiente)
   • Il voto finale viene calcolato automaticamente
   • Aggiungi note comportamentali specifiche
   • Modifica manualmente il giudizio se necessario
   ```

3. **Episodi Specifici**
   - Documenta episodi comportamentali significativi
   - Data, descrizione e gravità dell'episodio
   - Collegamento automatico al voto finale

### **Gestione Studenti Avanzata**

- **Modifica Rapida**: Doppio click per modificare nomi
- **Riordinamento**: Trascina per riordinare la lista
- **Eliminazione**: Pulsante elimina per rimuovere studenti
- **Duplicazione**: Copia impostazioni tra studenti simili

### **Generazione Report**

1. **Vista Risultati**
   ```
   Visualizza:
   • Tabella completa con tutti i voti
   • Indicatori comportamentali per studente
   • Note e osservazioni
   • Riepilogo statistico della classe
   ```

2. **Stampa/Export**
   ```
   Formati disponibili:
   📄 PDF: Documento ufficiale per scrutini
   📊 Excel: Dati strutturati per analisi
   🖨️ Stampa: Layout ottimizzato per carta A4
   ```

### **Statistiche Avanzate**

- **Distribuzione voti** per indicatore
- **Media classe** per comportamento generale
- **Trend temporali** se usata durante l'anno
- **Confronti** tra diverse valutazioni

## 🆘 Sistema di Aiuto Integrato

L'app include un **sistema di aiuto contestuale**:

1. **Pulsante "?" nell'Header**
   - Guida step-by-step per ogni funzione
   - Esempi pratici di utilizzo
   - Risoluzione problemi comuni

2. **Sezioni di Aiuto**
   ```
   📋 Configurazione: Setup iniziale dell'app
   👥 Gestione Studenti: Import e gestione elenchi
   🎯 Valutazione: Sistema di voto e indicatori
   📊 Statistiche: Analisi e report avanzati
   💾 Backup: Salvataggio e ripristino dati
   🖨️ Stampa: Preparazione documenti ufficiali
   ```

## 📁 Gestione Dati e Backup

### **Salvataggio Automatico**
- I dati vengono salvati automaticamente nel browser
- Backup ogni volta che modifichi qualcosa
- Recupero automatico in caso di chiusura imprevista

### **Export/Import Configurazioni**
```javascript
// Export configurazione completa
Pulsante "Esporta Configurazione" → File JSON

// Import configurazione
Pulsante "Importa Configurazione" → Seleziona file JSON
```

### **Backup di Sicurezza**
- **Backup Locale**: Salvato nel localStorage del browser
- **Export Dati**: File JSON con tutti i dati
- **Ripristino**: Da file precedenti o backup automatici

## 🔧 Personalizzazione

### **Indicatori Comportamentali**
```
Indicatori Standard Inclusi:
• Rispetto delle regole di classe
• Partecipazione attiva alle lezioni  
• Collaborazione con compagni
• Rispetto per materiali e ambiente
• Autoregolazione emotiva
• Responsabilità nei compiti

Personalizzazione:
• Aggiungi nuovi indicatori
• Modifica pesi per calcolo finale
• Cambia descrizioni dei livelli
```

### **Livelli di Valutazione**
```
Sistema Standard (6 Livelli):
10 = OTTIMO       (Comportamento esemplare)
9  = DISTINTO     (Comportamento molto positivo)  
8  = BUONO        (Comportamento generalmente corretto)
7  = DISCRETO     (Comportamento abbastanza corretto)
6  = SUFFICIENTE  (Comportamento accettabile)
5  = NON SUFFICIENTE (Comportamento problematico)
```

## 🖨️ Stampa e Documenti Ufficiali

### **Layout Stampa Ottimizzato**
- **Formato A4**: Margini e layout professionali
- **Intestazione Scuola**: Logo e dati istituto
- **Tabelle Leggibili**: Font e spaziature ottimizzate
- **Firma Coordinatore**: Spazio dedicato per firma

### **Documenti Generati**
1. **Griglia Valutazione Comportamento** (formato ministeriale)
2. **Riepilogo Classe** con statistiche
3. **Report Individuale** per singoli studenti
4. **Verbale Scrutinio** (su richiesta)

## 💡 Suggerimenti d'Uso

### **Best Practices**
```
✅ Configura sempre le informazioni scuola prima di iniziare
✅ Fai backup regolari esportando i dati
✅ Usa le note per episodi comportamentali significativi
✅ Personalizza gli indicatori per la tua classe
✅ Testa la stampa prima degli scrutini ufficiali
```

### **Workflow Consigliato**
```
1. Setup iniziale → Configura scuola e classe
2. Import studenti → Carica elenco da registro
3. Personalizza indicatori → Adatta alla tua programmazione
4. Valutazione periodica → Durante tutto l'anno
5. Scrutinio finale → Genera documenti ufficiali
```

## ❓ FAQ e Risoluzione Problemi

### **Domande Frequenti**

**Q: Come faccio il backup dei miei dati?**
A: Usa "Esporta Configurazione" per salvare tutto in un file JSON.

**Q: L'app funziona offline?**
A: Sì, una volta installata come PWA funziona completamente offline.

**Q: Posso personalizzare i livelli di valutazione?**
A: Sì, vai nelle impostazioni avanzate e modifica indicatori e pesi.

**Q: Come importo studenti da Registro Elettronico?**
A: Copia la lista nomi e incollala nel campo "Inserimento rapido studenti".

**Q: I dati sono sicuri?**
A: Sì, tutto viene salvato localmente sul tuo dispositivo. Nessun dato va online.

### **Problemi Comuni**

**❌ L'app non si installa come PWA**
```
Soluzioni:
• Usa Chrome o Safari
• Verifica connessione internet durante prima installazione
• Pulisci cache browser e ricarica
```

**❌ La stampa non è formattata bene**
```
Soluzioni:
• Usa "Anteprima di stampa" per verificare
• Imposta margini personalizzati se necessario
• Seleziona solo le sezioni necessarie
```

**❌ I dati non si salvano**
```
Soluzioni:
• Verifica spazio disponibile nel browser
• Non usare modalità incognito
• Fai export manuale come backup
```

## 🔄 Aggiornamenti e Versioning

### **Cronologia Versioni**
- **v1.0**: Versione base con valutazione comportamento
- **v1.1**: Aggiunto sistema PWA e installazione mobile
- **v1.2**: Sistema di aiuto integrato e guida contestuale
- **v1.3**: Export Excel e backup avanzati

### **Aggiornamenti Automatici**
- L'app si aggiorna automaticamente quando installi la PWA
- Notifiche per nuove funzionalità disponibili
- Compatibilità backward per dati esistenti

## 📞 Supporto e Feedback

### **Ottenere Aiuto**
1. **Guida Integrata**: Pulsante "?" nell'app
2. **Documentazione**: Questo file README
3. **Issues GitHub**: Per segnalare bug o richieste

### **Contributi**
- Fork del repository per miglioramenti
- Segnalazione bug e suggerimenti
- Traduzioni in altre lingue

## 📄 Licenza

Questo progetto è rilasciato sotto licenza MIT. Vedi il file [LICENSE](LICENSE) per dettagli.

---

## 🎯 Caratteristiche Tecniche

### **Tecnologie Utilizzate**
- **HTML5/CSS3**: Interface moderna e responsive
- **JavaScript Vanilla**: Nessuna dipendenza esterna
- **PWA**: Service Worker per funzionamento offline
- **Local Storage**: Salvataggio dati locale
- **Web APIs**: File reading, printing, export

### **Compatibilità Browser**
- ✅ Chrome 60+ (Raccomandato per PWA)
- ✅ Firefox 60+
- ✅ Safari 12+ (iOS)
- ✅ Edge 79+

### **Requisiti Sistema**
- **Spazio**: <5MB una volta installata
- **RAM**: Minimo 1GB 
- **Connessione**: Solo per prima installazione PWA

---

*Sviluppato per semplificare la valutazione comportamentale nella scuola primaria italiana 🇮🇹*