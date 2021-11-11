const Detection = () => {
  return (
    <>
      <section className="content-feature">
        <div className="content-feature-inner">
          <ul className="content-feature-inner-list">
            <li>AI TECH DEMO</li>
            <li print="here">IMAGE</li>
            <li print="here">물체 검출</li>
          </ul>
        </div>
      </section>
      <div className="content-detail">
        <h1>물체 검출</h1>
        <p>
          Image Detection은 ~~<br></br>
          부가사항
        </p>
        <div className="demo-visual">
          <div className="box_com image">
            <p>
              2MB 이하의 이미지를 올리거나<br></br>
              샘플을 선택해 결과를 확인해 보세요.
            </p>
            <button className="btn-q">샘플테스트</button>
          </div>
          <div className="box_com code">
              <ul className="code-select">
                  <li>
                      <button>TEXT</button>
                  </li>
                  <li>
                      <button>JSON</button>
                  </li>
              </ul>
          </div>
        </div>
      </div>
    </>
  );
};

export default Detection;
