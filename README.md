# ANSARI COMPANY Employee Handbook RAG

A simple retrieval-augmented generation (RAG) command-line app for asking questions about the bilingual (Arabic and English) ANSARI COMPANY employee handbook for Iraq. It retrieves relevant passages from `docs/handbook.md` and uses a local Ollama model to generate an answer.

## Requirements

- Python 3.11 or newer
- [uv](https://docs.astral.sh/uv/)
- [Ollama](https://ollama.com/) running locally at `http://localhost:11434`

The app is configured to use `nomic-embed-text:latest` for embeddings and `qwen3.8:latest` for chat. Make sure both models are available in your Ollama installation before starting the app.

## Setup

From the project directory, install the Python dependencies:

```powershell
uv sync
```

If you still need to download the configured Ollama models, run:

```powershell
ollama pull nomic-embed-text:latest
ollama pull qwen3.8:latest
```

Start the app from the project directory:

```powershell
uv run python rag.py
```

Enter a question at the `Question:` prompt. Submit an empty question to exit. The handbook is indexed when the app starts, so Ollama must be running before launch.

## Sample questions

1. What are the company's core values?
2. What should an employment contract include?
3. How many hours may employees normally work per day and per week?
4. How much annual leave is provided, and how should leave be requested?
5. What does the handbook say about sick leave and medical certificates?
6. What maternity leave and nursing protections are described?
7. Who should an employee contact when an illness or emergency prevents attendance?
8. How should employees report workplace complaints or harassment?
9. What are the expectations for protecting confidential company information?
10. What steps should be completed when an employee leaves the company?

## Important notice

The handbook is marked as a draft for management and legal review. The README and the app do not provide legal advice. Check answers against the handbook, the employee's contract, approved company policies, and applicable Iraqi law; mandatory law prevails over inconsistent handbook text. Company-specific fields in the handbook also need to be completed before it is issued.

---

# دليل الموظف - نظام RAG لشركة الأنصاري

تطبيق سطر أوامر بسيط يستخدم التوليد المعزز بالاسترجاع (RAG) للإجابة عن الأسئلة المتعلقة بدليل الموظف الثنائي اللغة (العربية والإنجليزية) لشركة الأنصاري في العراق. يسترجع التطبيق المقاطع ذات الصلة من `docs/handbook.md` ويستخدم نموذج Ollama محلياً لإنشاء الإجابة.

## المتطلبات

- Python 3.11 أو إصدار أحدث
- [uv](https://docs.astral.sh/uv/)
- تشغيل [Ollama](https://ollama.com/) محلياً على `http://localhost:11434`

تم إعداد التطبيق لاستخدام `nomic-embed-text:latest` لإنشاء التضمينات و`qwen3.8:latest` للمحادثة. تأكد من توفر النموذجين في تثبيت Ollama قبل تشغيل التطبيق.

## الإعداد

من مجلد المشروع، ثبّت تبعيات Python:

```powershell
uv sync
```

إذا لم تكن قد نزّلت نماذج Ollama المطلوبة بعد، فنفّذ:

```powershell
ollama pull nomic-embed-text:latest
ollama pull qwen3.8:latest
```

شغّل التطبيق من مجلد المشروع:

```powershell
uv run python rag.py
```

اكتب سؤالك عند ظهور المطالبة `Question:`. اضغط Enter على سؤال فارغ للخروج. تتم فهرسة الدليل عند بدء التطبيق، لذا يجب تشغيل Ollama قبل تشغيل التطبيق.

## أمثلة على الأسئلة

1. ما القيم الأساسية للشركة؟
2. ما المعلومات التي ينبغي أن يتضمنها عقد العمل؟
3. كم ساعة يجوز للموظف العمل عادةً في اليوم والأسبوع؟
4. ما مقدار الإجازة السنوية، وكيف ينبغي طلبها؟
5. ماذا يقول الدليل عن الإجازة المرضية والشهادات الطبية؟
6. ما أحكام إجازة الأمومة وحماية الرضاعة المذكورة؟
7. بمن ينبغي للموظف الاتصال إذا منعته حالة مرضية أو طارئة من الحضور؟
8. كيف يمكن للموظف الإبلاغ عن شكاوى مكان العمل أو التحرش؟
9. ما التوقعات المتعلقة بحماية معلومات الشركة السرية؟
10. ما الإجراءات التي ينبغي إكمالها عند مغادرة الموظف للشركة؟

## تنويه مهم

الدليل مسودة مخصصة لمراجعة الإدارة والمستشار القانوني. لا يقدم هذا الملف أو التطبيق استشارة قانونية. تحقّق من الإجابات بالرجوع إلى الدليل وعقد الموظف وسياسات الشركة المعتمدة والقانون العراقي النافذ؛ ويسود القانون الآمر عند تعارضه مع الدليل. كما يجب استكمال الحقول الخاصة بالشركة قبل إصدار الدليل.