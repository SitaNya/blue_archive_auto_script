import{_ as s,o as a,c as e,R as p}from"./chunks/framework.OPRPu5cH.js";const u=JSON.parse('{"title":"关于文档","description":"","frontmatter":{},"headers":[],"relativePath":"docs.md","filePath":"docs.md","lastUpdated":1700381800000}'),o={name:"docs.md"},n=p('<h1 id="关于文档" tabindex="-1">关于文档 <a class="header-anchor" href="#关于文档" aria-label="Permalink to &quot;关于文档&quot;">​</a></h1><p>当前文档使用<a href="https://vitepress.dev/" target="_blank" rel="noreferrer">VitePress</a>构建</p><p>为了编写文档，你可能需要准备<a href="https://nodejs.org/" target="_blank" rel="noreferrer">Nodejs</a>和<a href="https://pnpm.io/" target="_blank" rel="noreferrer">pnpm</a></p><h2 id="安装环境" tabindex="-1">安装环境 <a class="header-anchor" href="#安装环境" aria-label="Permalink to &quot;安装环境&quot;">​</a></h2><h3 id="安装node-js" tabindex="-1">安装Node.js <a class="header-anchor" href="#安装node-js" aria-label="Permalink to &quot;安装Node.js&quot;">​</a></h3><p>需要20.x版本</p><p>前往<a href="https://nodejs.org/" target="_blank" rel="noreferrer">Nodejs官网</a>下载安装包，安装完成后，打开命令行工具，输入 <code>node -v</code> 和 <code>npm -v</code> 检查是否安装成功</p><h3 id="安装pnpm" tabindex="-1">安装pnpm <a class="header-anchor" href="#安装pnpm" aria-label="Permalink to &quot;安装pnpm&quot;">​</a></h3><p>安装完Nodejs后</p><p>执行</p><div class="language-bash vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">bash</span><pre class="shiki github-dark vp-code-dark"><code><span class="line"><span style="color:#B392F0;">npm</span><span style="color:#E1E4E8;"> </span><span style="color:#9ECBFF;">install</span><span style="color:#E1E4E8;"> </span><span style="color:#79B8FF;">-g</span><span style="color:#E1E4E8;"> </span><span style="color:#9ECBFF;">pnpm</span></span></code></pre><pre class="shiki github-light vp-code-light"><code><span class="line"><span style="color:#6F42C1;">npm</span><span style="color:#24292E;"> </span><span style="color:#032F62;">install</span><span style="color:#24292E;"> </span><span style="color:#005CC5;">-g</span><span style="color:#24292E;"> </span><span style="color:#032F62;">pnpm</span></span></code></pre></div><h2 id="安装文档" tabindex="-1">安装文档 <a class="header-anchor" href="#安装文档" aria-label="Permalink to &quot;安装文档&quot;">​</a></h2><p>先切换到 <code>docs</code> 目录</p><div class="language-bash vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">bash</span><pre class="shiki github-dark vp-code-dark"><code><span class="line"><span style="color:#79B8FF;">cd</span><span style="color:#E1E4E8;"> </span><span style="color:#9ECBFF;">docs</span></span></code></pre><pre class="shiki github-light vp-code-light"><code><span class="line"><span style="color:#005CC5;">cd</span><span style="color:#24292E;"> </span><span style="color:#032F62;">docs</span></span></code></pre></div><p>安装依赖</p><div class="language-bash vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">bash</span><pre class="shiki github-dark vp-code-dark"><code><span class="line"><span style="color:#B392F0;">pnpm</span><span style="color:#E1E4E8;"> </span><span style="color:#9ECBFF;">install</span></span></code></pre><pre class="shiki github-light vp-code-light"><code><span class="line"><span style="color:#6F42C1;">pnpm</span><span style="color:#24292E;"> </span><span style="color:#032F62;">install</span></span></code></pre></div><h3 id="预览文档" tabindex="-1">预览文档 <a class="header-anchor" href="#预览文档" aria-label="Permalink to &quot;预览文档&quot;">​</a></h3><p>执行</p><div class="language-bash vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">bash</span><pre class="shiki github-dark vp-code-dark"><code><span class="line"><span style="color:#B392F0;">npm</span><span style="color:#E1E4E8;"> </span><span style="color:#9ECBFF;">run</span><span style="color:#E1E4E8;"> </span><span style="color:#9ECBFF;">docs:dev</span></span></code></pre><pre class="shiki github-light vp-code-light"><code><span class="line"><span style="color:#6F42C1;">npm</span><span style="color:#24292E;"> </span><span style="color:#032F62;">run</span><span style="color:#24292E;"> </span><span style="color:#032F62;">docs:dev</span></span></code></pre></div><p>实时预览文档</p><p>现在修改md文件试试！</p><h3 id="构建文档" tabindex="-1">构建文档 <a class="header-anchor" href="#构建文档" aria-label="Permalink to &quot;构建文档&quot;">​</a></h3><p>你需要部署文档？</p><p>执行</p><div class="language-bash vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">bash</span><pre class="shiki github-dark vp-code-dark"><code><span class="line"><span style="color:#B392F0;">npm</span><span style="color:#E1E4E8;"> </span><span style="color:#9ECBFF;">run</span><span style="color:#E1E4E8;"> </span><span style="color:#9ECBFF;">docs:build</span></span></code></pre><pre class="shiki github-light vp-code-light"><code><span class="line"><span style="color:#6F42C1;">npm</span><span style="color:#24292E;"> </span><span style="color:#032F62;">run</span><span style="color:#24292E;"> </span><span style="color:#032F62;">docs:build</span></span></code></pre></div><p>将会在 <code>docs/.vitepress/dist</code> 目录下生成静态文件</p>',26),l=[n];function t(c,r,d,i,h,y){return a(),e("div",null,l)}const E=s(o,[["render",t]]);export{u as __pageData,E as default};
