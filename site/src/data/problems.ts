import fs from 'node:fs';
import path from 'node:path';

export interface Problem {
  number: string;
  title: string;
  slug: string;
  dirName: string;
  category: string;
  statementEn: string | null;
  statementEs: string | null;
  solutionCode: string | null;
  solutionFile: string | null;
  prevSlug: string | null;
  nextSlug: string | null;
}

export interface Category {
  name: string;
  problems: Problem[];
}

const ROOT = path.resolve(import.meta.dirname, '..', '..', '..');

function findPythonFile(dirPath: string): { name: string; code: string } | null {
  if (!fs.existsSync(dirPath)) return null;
  const files = fs.readdirSync(dirPath).filter(f =>
    f.endsWith('.py') && fs.statSync(path.join(dirPath, f)).isFile()
  );
  if (files.length === 0) return null;

  for (const file of files) {
    const content = fs.readFileSync(path.join(dirPath, file), 'utf-8');
    if (content.trim().length > 0) {
      return { name: file, code: content };
    }
  }
  return null;
}

function extractEnglishStatement(mdContent: string): string {
  // Find the English section start
  const englishStart = mdContent.search(/^## .*(English|english)/m);
  if (englishStart === -1) return mdContent;

  const afterEnglish = mdContent.slice(englishStart);

  // Find the end: either a --- separator or the Spanish section
  const endMatch = afterEnglish.search(/\n---\n|^## .*(Español|español|Espa)/m);

  let englishSection: string;
  if (endMatch === -1) {
    englishSection = afterEnglish;
  } else {
    englishSection = afterEnglish.slice(0, endMatch);
  }

  // Remove the English heading itself
  englishSection = englishSection.replace(/^## .*\n+/, '');

  return englishSection.trim();
}

function extractSpanishStatement(mdContent: string): string | null {
  const spanishStart = mdContent.search(/^## .*(Español|español|Espa)/m);
  if (spanishStart === -1) return null;

  let spanishSection = mdContent.slice(spanishStart);
  // Remove the Spanish heading itself
  spanishSection = spanishSection.replace(/^## .*\n+/, '');

  return spanishSection.trim();
}

function parseReadme(): Category[] {
  const readme = fs.readFileSync(path.join(ROOT, 'README.md'), 'utf-8');
  const categories: Category[] = [];

  // Split by ### headings (categories)
  const sections = readme.split(/^### /m).slice(1);

  for (const section of sections) {
    const lines = section.split('\n');
    const categoryName = lines[0].trim();
    const problems: Problem[] = [];

    // Parse table rows: | 01 | Two Sum | [two_sum.py](01-two-sum/) |
    const rowRegex = /^\|\s*(\d+)\s*\|\s*(.+?)\s*\|\s*\[.*?\]\((.+?)\/?(\))\s*\|/;

    for (const line of lines) {
      const match = line.match(rowRegex);
      if (!match) continue;

      const [, number, title, dirName] = match;
      const slug = dirName.replace(/\/$/, '');

      // Read statement.md
      const statementPath = path.join(ROOT, dirName, 'statement.md');
      let statementEn: string | null = null;
      let statementEs: string | null = null;
      if (fs.existsSync(statementPath)) {
        const mdContent = fs.readFileSync(statementPath, 'utf-8');
        statementEn = extractEnglishStatement(mdContent);
        statementEs = extractSpanishStatement(mdContent);
      }

      // Find Python solution file
      const pyFile = findPythonFile(path.join(ROOT, dirName));

      problems.push({
        number: number.padStart(2, '0'),
        title: title.trim(),
        slug,
        dirName,
        category: categoryName,
        statementEn,
        statementEs,
        solutionCode: pyFile?.code ?? null,
        solutionFile: pyFile?.name ?? null,
        prevSlug: null,
        nextSlug: null,
      });
    }

    if (problems.length > 0) {
      categories.push({ name: categoryName, problems });
    }
  }

  // Compute prev/next across all problems
  const allProblems = categories.flatMap(c => c.problems);
  for (let i = 0; i < allProblems.length; i++) {
    allProblems[i].prevSlug = i > 0 ? allProblems[i - 1].slug : null;
    allProblems[i].nextSlug = i < allProblems.length - 1 ? allProblems[i + 1].slug : null;
  }

  return categories;
}

let cachedCategories: Category[] | null = null;

export function getCategories(): Category[] {
  if (!cachedCategories) {
    cachedCategories = parseReadme();
  }
  return cachedCategories;
}

export function getAllProblems(): Problem[] {
  return getCategories().flatMap(c => c.problems);
}

export function getProblemBySlug(slug: string): Problem | undefined {
  return getAllProblems().find(p => p.slug === slug);
}
