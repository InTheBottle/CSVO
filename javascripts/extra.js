document$.subscribe(function () {
    const $hero = document.querySelector(".background-hero");

    if ($hero) {
        console.log("GSAP Version:", gsap.version);

        let xTo = gsap.quickTo($hero, "x", { duration: 1, ease: "power3.out" });
        let yTo = gsap.quickTo($hero, "y", { duration: 1, ease: "power3.out" });
        let rotXTo = gsap.quickTo($hero, "rotationX", { duration: 1, ease: "power3.out" });
        let rotYTo = gsap.quickTo($hero, "rotationY", { duration: 1, ease: "power3.out" });

        window.addEventListener("mousemove", (e) => {
            const mouseX = e.clientX / window.innerWidth - 0.5;
            const mouseY = e.clientY / window.innerHeight - 0.5;

            xTo(mouseX * 50);
            yTo(mouseY * 50);
            rotYTo(mouseX * 5);
            rotXTo(-mouseY * 5);
        });
    }
});
